import boto3
from django.shortcuts import render
from aws.forms import DashboardForm
from aws.models import AppsDescription


def index(request):
    return render(request, "index.html")


def dashboardform(request):

    new_dict = aws_list_conf_api_call()

    return render(request, "dashboard.html", {'aws_response': new_dict})



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

    return new_dict


def createapp(request):
    form = DashboardForm()

    if request.method == "POST":
        form = DashboardForm(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return render(request, "success.html")

    return render(request, "createapp.html", {'form':form})


def manageapp(request):
    apps = AppsDescription.objects.order_by("name")
    return render(request, "manageapp.html", {"apps":apps})