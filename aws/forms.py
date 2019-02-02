import boto3
from django import forms
from aws.models import AppsDescription, InfraServiceInfo


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


class DashboardForm(forms.ModelForm):
    class Meta():
        model = AppsDescription
        fields = '__all__'


class InfraForm(forms.ModelForm):
    class Meta():
        model = InfraServiceInfo
        fields = '__all__'