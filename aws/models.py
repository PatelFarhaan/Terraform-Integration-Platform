from django.db import models as db
from django.db.models import CharField
from django_mysql.models import ListCharField


class AppsDescription(db.Model):
    SERVER_CHOICES = []


    CHOICES = [("yes", "YES"),
               ("no", "NO")]
    OPTIONS = list()


    name = db.CharField(max_length=256, unique=True)
    description = db.TextField()
    plan_to_migrate = db.CharField(choices=CHOICES, max_length=256)
    server_names = db.TextField(null=True)
    create_app_response = db.TextField(null=True)

    def __str__(self):
        return self.name



class StaticData(db.Model):

    stack = CharField(max_length=1000)
    description = CharField(max_length=1000)


class StaticData2(db.Model):

    instance_type = ListCharField(base_field=CharField(max_length=1000), max_length=1000)
    instance_number = ListCharField(base_field=CharField(max_length=1000), max_length=1000)
    engine = ListCharField(base_field=CharField(max_length=1000), max_length=1000)


class InfraServiceInfo(db.Model):

    AppsDescription_names = AppsDescription.objects.all()
    ins_choice = StaticData.objects.all()
    ins_choices = StaticData2.objects.all()
    DESC_CHOICES = list()


    for i in ins_choices:
        global INS_CHOICES, INS_TYPE
        INS_CHOICES = i.instance_number
        INS_TYPE = i.instance_type

    stack_choice = []
    for i in ins_choice:
        global STACK_CHOICE
        stack_choice.append(i.stack)

    VIEW_APP_CHOICES = list()
    VIEW_DESC_CHOICES = list()
    VIEW_NO_INS_CHOICES = []
    VIEW_STACK_CHOICES = []
    VIEW_INS_TYPE = []

    for app_names in AppsDescription_names:
        VIEW_APP_CHOICES.append(('{}'.format(app_names.name), '{}'.format(app_names.name)), )
    for app_names in INS_CHOICES:
        VIEW_NO_INS_CHOICES.append(("{}".format(app_names), "{}".format(app_names)))
    for app_names in stack_choice:
        VIEW_STACK_CHOICES.append(("{}".format(app_names), "{}".format(app_names)))
    for app_names in INS_TYPE:
        VIEW_INS_TYPE.append(("{}".format(app_names), "{}".format(app_names)))

    app_name = db.ForeignKey(AppsDescription, on_delete=db.CASCADE)
    env_name = db.CharField(max_length=1000, unique=True)
    stack = db.CharField(choices=VIEW_STACK_CHOICES, max_length=1000)
    description = db.CharField(max_length=1000, blank=True)
    no_of_instance = db.CharField(choices=VIEW_NO_INS_CHOICES, max_length=256)
    instance_type = db.CharField(choices=VIEW_INS_TYPE, max_length=256)
    ssh_location = db.GenericIPAddressField(default='192.168.1.2')
    app_id = db.CharField(max_length=1000, null=True)
    output_json_status = db.CharField(max_length=10000, blank=True, default="In Progress")

    def __str__(self):
        return self.env_name


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

    engine_list = StaticData2.objects.all()
    ins_choice = StaticData2.objects.all()

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
    env_id = db.CharField(max_length=1000, null=True)


class InfraCicd(db.Model):

    TYPE_CHOICES = [
        ("s3", "s3"),
        ("code commit", "code commit")
    ]

    source_repo = db.CharField(choices=TYPE_CHOICES, max_length=1000)
    name = db.CharField(max_length=1000)
    app_id = db.CharField(max_length=1000, null=True)


class CreateMigrations(db.Model):


    ENGINE_NAMES = [('MySQL', 'MySQL'),
                    ('Oracle', 'Oracle')]

    app_name = db.ForeignKey(AppsDescription, on_delete=db.CASCADE)
    env_name = db.ForeignKey(InfraServiceInfo, on_delete=db.CASCADE)
    destination_db = db.CharField(max_length=1000, blank=True)
    source_ip = db.GenericIPAddressField(default='192.168.1.2')
    source_username = db.CharField(max_length=1000)
    source_password = db.CharField(max_length=1000)
    source_db = db.CharField(max_length=1000)
    engine_name = db.CharField(choices=ENGINE_NAMES, max_length=1000, blank=True)



class Ec2(db.Model):

    ec2_instancetype = db.CharField(max_length=1000)
    ec2_count = db.CharField(max_length=1000)
    ec2_ami = db.CharField(max_length=1000)
    ec2_environment = db.CharField(max_length=1000)
    ec2_appname = db.CharField(max_length=1000)
    ec2_environment_id = db.CharField(max_length=1000)
    ec2_public_dns = db.CharField(max_length=10000, blank=True)
    ec2_dns = db.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.ec2_appname


class Rds(db.Model):

    rds_engine = db.CharField(max_length=1000)
    rds_instance = db.CharField(max_length=1000)
    rds_storage = db.CharField(max_length=1000)
    rds_username = db.CharField(max_length=1000)
    rds_password = db.CharField(max_length=1000)
    rds_appname = db.CharField(max_length=1000)
    rds_environment = db.CharField(max_length=1000)
    rds_environment_id = db.CharField(max_length=1000)
    rds_database = db.CharField(max_length=10000, blank=True)
    rds_endpoint = db.CharField(max_length=10000, blank=True)
    rds_json_username = db.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.rds_environment


class Cicd(db.Model):

    cicd_appname = db.CharField(max_length=1000)
    repo_name = db.CharField(max_length=1000)
    env_name = db.CharField(max_length=1000)
    cicd_env_id = db.CharField(max_length=1000)
    s3_artifact_bucket = db.CharField(max_length=1000)
    cicd_artifact = db.CharField(max_length=10000, blank=True)
    cicd_repo_http =db.CharField(max_length=10000, blank=True)
    cicd_repo_ssh = db.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.cicd_appname