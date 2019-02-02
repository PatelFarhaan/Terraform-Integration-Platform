import boto3
from django.db import models as db
from multiselectfield import MultiSelectField



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


class AppsDescription(db.Model):
    aws_response = aws_list_conf_api_call()

    CHOICES = [("yes", "YES"),
               ("no", "NO")]
    OPTIONS = list()

    for apps in aws_response:
        OPTIONS.append(('{name1}'.format(name1=apps.lower()), '{name2}'.format(name2=apps)), )

    name = db.CharField(max_length=256)
    description = db.TextField()
    plan_to_migrate = db.CharField(choices=CHOICES, max_length=256)
    app_names = MultiSelectField(choices=OPTIONS)

    def __str__(self):
        return self.name


class InfraServiceInfo(db.Model):

    aws_response = aws_list_conf_api_call2()
    APP_CHOICES = list()
    DESC_CHOICES = list()
    NO_INS_CHOICES = list()

    VIEW_APP_CHOICES = list()
    VIEW_DESC_CHOICES = list()
    VIEW_NO_INS_CHOICES = list()


    for i in aws_response:
        APP_CHOICES.append(i["name"])
        DESC_CHOICES.append(i["description"])
        NO_INS_CHOICES.append(i["serverCount"])

    for app_names in APP_CHOICES:
        VIEW_APP_CHOICES.append(('{}'.format(app_names.lower()), '{}'.format(app_names)), )
    for app_names in DESC_CHOICES:
        VIEW_DESC_CHOICES.append(('{}'.format(app_names.lower()), '{}'.format(app_names)), )
    for app_names in NO_INS_CHOICES:
        VIEW_NO_INS_CHOICES.append(('{}'.format(app_names.lower()), '{}'.format(app_names)), )

    app_name = db.CharField(choices=VIEW_APP_CHOICES, max_length=1000)
    env_name = db.CharField(max_length=1000)
    stack = db.CharField(max_length=1000)
    description = db.TextField(choices=VIEW_DESC_CHOICES)
    no_of_instance = db.CharField(choices=VIEW_NO_INS_CHOICES, max_length=256)
    instance_type = db.CharField(max_length=256)
    ssh_location = db.GenericIPAddressField()

    def __str__(self):
        return self.app_name