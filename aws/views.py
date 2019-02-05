import os
import json
import boto3
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from aws.forms import DashboardForm, InfraForm
from aws.models import AppsDescription, InfraServiceInfo, ServerAwsInfo



def index(request):
    return render(request, "index.html")


def dashboardform(request):

    new_dict = aws_list_conf_api_call()
    return render(request, "dashboard.html", {'aws_response': new_dict})


def aws_applicationId_status(applicationId):
    client = boto3.client('mgh', region_name='us-west-2')
    response = client.describe_application_state(
        ApplicationId = applicationId
    )
    return response['ApplicationStatus']


def create_aws_app(name, description):
    client = boto3.client('discovery', region_name='us-west-2')

    response = client.create_application(
        name=name,
        description=description
    )

    return response

def aws_server_list_conf():
    client = boto3.client('discovery', region_name='us-west-2')
    response = client.list_configurations(
        configurationType="SERVER",
        filters=[]
    )

    count = list()
    key_list = list()
    value_list = list()

    for i in response['configurations']:
        count.append(len(i))

    new_dict = list()

    for k, v in response.items():
        if k == 'configurations':
            for b in range(len(count)):
                for k1, v1 in v[b].items():
                    key_list.append(k1[7:])
                    value_list.append(v1)

                new_dict.append(dict(zip(key_list, value_list)))

    return new_dict


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

    for i in new_dict:
        i['app_status'] = aws_applicationId_status(i['configurationId'])

    return new_dict


def ec2_json(ins_type, ins_count, ins_ami, ins_env, app_name, env_id, location):
    data = {"ec2_instancetype":"{}".format(ins_type),
    "ec2_count":"{}".format(ins_count),
    "ec2_ami":"{}".format(ins_ami),
    "ec2_environment":"{}".format(ins_env),
    "ec2_appname":"{}".format(app_name),
    "ec2_environment_id":"{}".format(env_id)}

    json_data = json.dumps(data)

    file = open(location+'/ec2.tfvars.json', 'w')

    for i in json_data:
        file.write(i)

    file.close()


def createapp(request):

    ServerAwsInfo.objects.all().delete()
    server_response = aws_server_list_conf()
    for i in server_response:
        ServerAwsInfo.objects.create(**i)


    form = DashboardForm()

    if request.method == "POST":
        form = DashboardForm(request.POST)
        server_id = request.POST.getlist('serverId')

        if form.is_valid:

            if form.data["plan_to_migrate"] == 'yes':
                create_app_resp = create_aws_app(form.data['name'], form.data['description'])
                AppsDescription.objects.create(name=form.data["name"],
                                                     description=form.data["description"],
                                                     plan_to_migrate=form.data["plan_to_migrate"],
                                                     server_names=server_id,
                                                     create_app_response=create_app_resp)
                return HttpResponseRedirect(reverse("aws:createapp"))
            else:
                AppsDescription.objects.create(name=form.data["name"],
                                               description=form.data["description"],
                                               plan_to_migrate=form.data["plan_to_migrate"],
                                               server_names=server_id)
                return HttpResponseRedirect(reverse("aws:createapp"))

    server = ServerAwsInfo.objects.all()
    return render(request, "createapp.html", {'server':server, 'form': form})


def manageapp(request):

    # AppsDescription.objects.all().delete()

    if request.method == "POST":
        app_name = request.POST.get('appname')
        AppsDescription.objects.filter(name=app_name).first().delete()


    apps = AppsDescription.objects.order_by("-id")
    return render(request, "manageapp.html", {"apps":apps})


def manageenv(request):
    return render(request, "manageenv.html")


def infraCompute(request):


    # import ipdb; ipdb.set_trace()
    form = InfraForm()

    if request.method == "POST":
        form = InfraForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #  /home/ec2-user/<appid>/<envid>/<envname>/

            app_name = form.data['app_name']
            env_name = form.data['env_name']
            new_env_name = ''.join(env_name.split())


            app_id = AppsDescription.objects.get(name=app_name).id
            env_id = InfraServiceInfo.objects.get(env_name=env_name).id



            try:
                aws_home_folder_location = '/home/ec2-user/{ai}/{ei}/{en}'.format(ai=app_id,
                                                                                 ei=env_id,
                                                                                 en=new_env_name)

                original_umask = os.umask(0)
                os.makedirs(aws_home_folder_location, mode=0o777)
            finally:
                os.umask(original_umask)

            ec2_json(form.data['instance_type'],
                     form.data['no_of_instance'],
                     form.data['stack'],
                     new_env_name,
                     app_name,
                     env_id,
                     aws_home_folder_location)



            return HttpResponseRedirect(reverse("aws:createenv"))

    return render(request, "infraservice.html", {'form': form})