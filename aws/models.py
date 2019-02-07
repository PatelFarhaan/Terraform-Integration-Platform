import boto3
from django.db import models as db
from django.db.models import CharField
from django_mysql.models import ListCharField



def aws_server_list_conf():
    client = boto3.client('discovery', region_name='us-west-2')
    response = client.list_configurations(
        configurationType="SERVER",
        filters=[]
    )

    server_id_list = list()

    for i in response['configurations']:
        server_id_list.append(i['server.configurationId'])

    return server_id_list


def aws_list_conf_api_call():

    client = boto3.client('discovery', region_name='us-west-2')

    aws_response = client.list_configurations(

        configurationType="APPLICATION",
        filters=[]

    )

    count = []
    key_list = []
    value_list = []

    for i in aws_response['configurations']:
        count.append(len(i))

    new_dict = list()

    for k, v in aws_response.items():
        if k == 'configurations':
            for b in range(len(count)):
                for k1, v1 in v[b].items():
                    key_list.append(k1[12:])
                    value_list.append(v1)

                new_dict.append(dict(zip(key_list, value_list)))

    name_list = list()

    for i in new_dict:
        name_list.append(i['name'])

    return name_list


def aws_list_conf_api_call2():

    client = boto3.client('discovery', region_name='us-west-2')

    aws_response = client.list_configurations(

        configurationType="APPLICATION",
        filters=[]

    )

    count = []
    key_list = []
    value_list = []

    for i in aws_response['configurations']:
        count.append(len(i))

    new_dict = list()

    for k, v in aws_response.items():
        if k == 'configurations':
            for b in range(len(count)):
                for k1, v1 in v[b].items():
                    key_list.append(k1[12:])
                    value_list.append(v1)

                new_dict.append(dict(zip(key_list, value_list)))


    return new_dict

#######################################################################################################################



class AppsDescription(db.Model):
    aws_response = aws_list_conf_api_call()
    server_response = aws_server_list_conf()

    SERVER_CHOICES = []

    for i in server_response:
        SERVER_CHOICES.append(('{lower}'.format(lower=i), '{upper}'.format(upper=i)), )

    CHOICES = [("yes", "YES"),
               ("no", "NO")]
    OPTIONS = list()

    for apps in aws_response:
        OPTIONS.append(('{name1}'.format(name1=apps), '{name2}'.format(name2=apps)), )

    name = db.CharField(max_length=256, unique=True)
    description = db.TextField()
    plan_to_migrate = db.CharField(choices=CHOICES, max_length=256)
    server_names = db.TextField(null=True)
    create_app_response = db.TextField(null=True)

    def __str__(self):
        return self.name


class StaticData(db.Model):

    stack = ListCharField(base_field=CharField(max_length=1000), max_length=1000)
    description = ListCharField(base_field=CharField(max_length=1000), max_length=1000)
    instance_type = ListCharField(base_field=CharField(max_length=1000), max_length=1000)
    instance_number = ListCharField(base_field=CharField(max_length=1000), max_length=1000)
    engine = ListCharField(base_field=CharField(max_length=1000), max_length=1000)


class InfraServiceInfo(db.Model):

    AppsDescription_names = AppsDescription.objects.all()
    ins_choice = StaticData.objects.all()
    aws_response = aws_list_conf_api_call2()
    DESC_CHOICES = list()


    for i in ins_choice:
        global STACK_CHOICE, INS_CHOICES, INS_TYPE
        STACK_CHOICE = i.stack
        INS_CHOICES = i.instance_number
        INS_TYPE = i.instance_type


    VIEW_APP_CHOICES = list()
    VIEW_DESC_CHOICES = list()
    VIEW_NO_INS_CHOICES = []
    VIEW_STACK_CHOICES = []
    VIEW_INS_TYPE = []


    for i in aws_response:
        DESC_CHOICES.append(i["description"])


    for app_names in AppsDescription_names:
        VIEW_APP_CHOICES.append(('{}'.format(app_names.name), '{}'.format(app_names.name)), )
    for app_names in INS_CHOICES:
        VIEW_NO_INS_CHOICES.append(("{}".format(app_names), "{}".format(app_names)))
    for app_names in STACK_CHOICE:
        VIEW_STACK_CHOICES.append(("{}".format(app_names), "{}".format(app_names)))
    for app_names in INS_TYPE:
        VIEW_INS_TYPE.append(("{}".format(app_names), "{}".format(app_names)))

    app_name = db.CharField(choices=VIEW_APP_CHOICES, max_length=1000)
    env_name = db.CharField(max_length=1000, unique=True)
    stack = db.CharField(choices=VIEW_STACK_CHOICES, max_length=1000)
    description = db.TextField(blank=True)
    no_of_instance = db.CharField(choices=VIEW_NO_INS_CHOICES, max_length=256)
    instance_type = db.CharField(choices=VIEW_INS_TYPE, max_length=256)
    ssh_location = db.GenericIPAddressField(default='192.168.1.2')

    def __str__(self):
        return self.app_name


class ServerAwsInfo(db.Model):

    agentId = db.CharField(max_length=1000)
    configurationId = db.CharField(max_length=1000)
    hostName = db.CharField(max_length=1000)
    osName = db.CharField(max_length=1000)
    osVersion = db.CharField(max_length=1000)
    source = db.CharField(max_length=1000)
    timeOfCreation = db.CharField(max_length=1000)
    type = db.CharField(max_length=1000)

    def __str__(self):
        return self.hostName


class InfraDatabases(db.Model):

    engine_list = StaticData.objects.all()
    ins_choice = StaticData.objects.all()

    for i in ins_choice:
        global INS_TYPE
        INS_TYPE = i.instance_type

    VIEW_INS_TYPE = []

    for app_names in INS_TYPE:
        VIEW_INS_TYPE.append(("{}".format(app_names), "{}".format(app_names)))

    for i in engine_list:
        global ENG
        ENG = i.engine

        VIEW_ENG_LIST = list()
        for app_names in ENG:
            VIEW_ENG_LIST.append(("{}".format(app_names), "{}".format(app_names)))


    engine = db.CharField(choices=VIEW_ENG_LIST, max_length=1000)
    db_instance_class = db.CharField(choices=VIEW_INS_TYPE, max_length=1000)
    username = db.CharField(max_length=256)
    password = db.CharField(max_length=1000)
    volume_size = db.PositiveIntegerField(default=0)


class InfraCicd(db.Model):

    TYPE_CHOICES = [
        ("s3", "s3"),
        ("code commit", "code commit")
    ]

    source_repo = db.CharField(choices=TYPE_CHOICES, max_length=1000)
    name = db.CharField(max_length=1000)


class CreateMigrations(db.Model):

    app_names = AppsDescription.objects.all()
    VIEW_APP_CHOICES = []
    for app_name in app_names:
        VIEW_APP_CHOICES.append(('{}'.format(app_name.name), '{}'.format(app_name.name)), )

    env_names = InfraServiceInfo.objects.all()
    VIEW_ENV_CHOICES = []
    for app_names in env_names:
        VIEW_ENV_CHOICES.append(('{}'.format(app_names.env_name), '{}'.format(app_names.env_name)), )

    db_names = InfraDatabases.objects.all()
    VIEW_DB_CHOICES = []
    for app_names in db_names:
        VIEW_DB_CHOICES.append(('{}'.format(app_names.engine), '{}'.format(app_names.engine)), )


    app_name = db.CharField(choices=VIEW_APP_CHOICES, max_length=1000)
    env_name = db.CharField(choices=VIEW_ENV_CHOICES, max_length=1000)
    source_ip = db.GenericIPAddressField(default='192.168.1.2')
    source_username = db.CharField(max_length=1000)
    source_password = db.CharField(max_length=1000)
    source_db = db.CharField(max_length=1000)
    destination_db = db.CharField(choices=VIEW_DB_CHOICES, max_length=1000)