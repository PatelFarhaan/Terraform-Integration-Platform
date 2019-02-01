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