import os
import json
import boto3
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from aws.forms import DashboardForm,InfraDatabase,InfraForm, InfraCicds, CreateMigrationForm
from aws.models import StaticData, AppsDescription, ServerAwsInfo, InfraServiceInfo, Ec2, Rds, Cicd, CreateMigrations


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
    data = {
    "ec2_instancetype":"{}".format(ins_type),
    "ec2_count":"{}".format(ins_count),
    "ec2_ami":"{}".format(ins_ami),
    "ec2_environment":"{}".format(ins_env),
    "ec2_appname":"{}".format(app_name),
    "ec2_environment_id":"{}".format(env_id)
    }

    json_data = json.dumps(data)

    file = open(location+'/ec2.tfvars.json', 'w')

    for i in json_data:
        file.write(i)

    file.close()


def db_json(rds_eng, ins_type, red_store, rds_user, rds_pass, app_name, rds_env, rds_env_id, location):
    data = {
        "rds_engine":"{}".format(rds_eng),
        "rds_instance":"{}".format(ins_type),
        "rds_storage":"{}".format(red_store),
        "rds_username":"{}".format(rds_user),
        "rds_password":"{}".format(rds_pass),
        "rds_appname":"{}".format(app_name),
        "rds_environment":"{}".format(rds_env),
        "rds_environment_id":"{}".format(rds_env_id)
    }

    json_data = json.dumps(data)

    file = open(location+'/rds.tfvars.json', 'w')

    for i in json_data:
        file.write(i)

    file.close()


def cicd_json(app_name, repo_name, env_name, env_id, bucket, location):
    data = {
        "cicd_appname":"{}".format(app_name),
        "repo_name":"{}".format(repo_name),
        "env_name":"{}".format(env_name),
        "cicd_env_id":"{}".format(env_id),
        "s3_artifact_bucket":"{}".format(bucket)
    }

    json_data = json.dumps(data)

    file = open(location + '/cicd.tfvars.json', 'w')

    for i in json_data:
        file.write(i)

    file.close()


def dms_json(app_name, env_name, env_id, source_ip, port, username, password, enginename, location):
    data = {
        "dms_appname":"{}".format(app_name),
        "dms_envname":"{}".format(env_name),
        "dms_envid":"{}".format(env_id),
        "dms_src_servername":"{}".format(source_ip),
        "dms_src_port":"{}".format(port),
        "dms_src_username": "{}".format(username),
        "dms_src_password": "{}".format(password),
        "dms_src_enginename": "{}".format(enginename)
    }

    json_data = json.dumps(data)

    file = open(location + '/dms.tfvars.json', 'w')

    for i in json_data:
        file.write(i)

    file.close()


def createapp(request):

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
                return HttpResponseRedirect(reverse("aws:manageapp"))
            else:
                AppsDescription.objects.create(name=form.data["name"],
                                               description=form.data["description"],
                                               plan_to_migrate=form.data["plan_to_migrate"],
                                               server_names=server_id)
                return HttpResponseRedirect(reverse("aws:manageapp"))

    server = ServerAwsInfo.objects.all()
    return render(request, "createapp.html", {'server':server, 'form': form})


def manageapp(request):

    if request.method == "POST":
        app_name = request.POST.get('appname')
        AppsDescription.objects.filter(name=app_name).first().delete()


    apps = AppsDescription.objects.order_by("-id")
    return render(request, "manageapp.html", {"apps":apps})


def manageenv(request):

    if request.method == "POST":
        env_obj = InfraServiceInfo.objects.order_by("-id")
        env_id = request.POST.get("envid")
        obj = InfraServiceInfo.objects.get(id=env_id)
        ai = obj.app_id
        en = obj.env_name
        path = '/home/ec2-user/{ai}/{ei}/{en}/'.format(ai=ai,ei=env_id,en=en)
        file_ec2 = 'ec2.tfvars.json'
        f1 = json.loads(open(path+file_ec2, "r").read())
        file_ec2 = 'rds.tfvars.json'
        f2 = json.loads(open(path + file_ec2, "r").read())
        file_ec2 = 'cicd.tfvars.json'
        f3 = json.loads(open(path + file_ec2, "r").read())

        Ec2.objects.all().delete()
        Ec2.objects.create(**f1)

        Rds.objects.all().delete()
        Rds.objects.create(**f2)

        Cicd.objects.all().delete()
        Cicd.objects.create(**f3)

        ec2 = Ec2.objects.all()
        rds = Rds.objects.all()
        cicd = Cicd.objects.all()


        status_result = None
        try:
            status_result = json.loads(open(path+"failure_apply.json", "r").read())['status']
        except:
            status_result = json.loads(open(path+"success_apply.json", "r").read())['status']

        if status_result == 'success':

            InfraServiceInfo.objects.filter(id=env_id).update(output_json_status=status_result)

            file_output_json = 'output.json'
            f3 = json.loads(open(path + file_output_json, "r").read())

            cicd_artifact = f3['CICD_Artifact Bucket']['value']
            cicd_repo_http = f3['CICD_Repo HTTP URL']['value']
            cicd_repo_ssh = f3['CICD_Repo SSH URL']['value']
            ec2_elb_dns = f3['EC2_ELB Public Dns']['value']
            ec2_public_dns = f3['EC2_Server Public DNS']['value']
            rds_database = f3['RDS_Database Name']['value']
            rds_endpoint = f3['RDS_Endpoint']['value']
            rds_username = f3['RDS_User Name']['value']


            ec2_obj = Ec2.objects.all()
            for i in ec2_obj:
                id1 = i.id
            Ec2.objects.filter(id=id1).update(ec2_public_dns=ec2_public_dns,
                                              ec2_dns=ec2_elb_dns)

            rds_obj = Rds.objects.all()
            for i in rds_obj:
                id2 = i.id
            Rds.objects.filter(id=id2).update(rds_database=rds_database,
                                              rds_endpoint=rds_endpoint,
                                              rds_json_username=rds_username)

            cicd_obj = Cicd.objects.all()
            for i in cicd_obj:
                id3 = i.id
            Cicd.objects.filter(id=id3).update(cicd_artifact=cicd_artifact,
                                               cicd_repo_http=cicd_repo_http,
                                               cicd_repo_ssh=cicd_repo_ssh)



        if status_result == 'failed':

            InfraServiceInfo.objects.filter(id=env_id).update(output_json_status=status_result)

            cicd_artifact = ''
            cicd_repo_http = ''
            cicd_repo_ssh = ''
            ec2_elb_dns = ''
            ec2_public_dns = ''
            rds_database = ''
            rds_endpoint = ''
            rds_username = ''

            ec2_obj = Ec2.objects.all()
            for i in ec2_obj:
                id1 = i.id
            Ec2.objects.filter(id=id1).update(ec2_public_dns=ec2_public_dns,
                                              ec2_dns=ec2_elb_dns)

            rds_obj = Rds.objects.all()
            for i in rds_obj:
                id2 = i.id
            Rds.objects.filter(id=id2).update(rds_database=rds_database,
                                              rds_endpoint=rds_endpoint,
                                              rds_json_username=rds_username)

            cicd_obj = Cicd.objects.all()
            for i in cicd_obj:
                id3 = i.id
            Cicd.objects.filter(id=id3).update(cicd_artifact=cicd_artifact,
                                               cicd_repo_http=cicd_repo_http,
                                               cicd_repo_ssh=cicd_repo_ssh)


        return render(request, "manageenv.html", {"ec2":ec2, "rds":rds, "cicd":cicd, "env":env_obj})

    else:

        env_obj = InfraServiceInfo.objects.order_by("-id")

    return render(request, "manageenv.html", {"env": env_obj})


def infraCompute(request):

    form = InfraForm()

    if request.method == "POST":
        form = InfraForm(request.POST)

        if form.is_valid():
            current_form = form.save(commit=False)
            app_name = form.data['app_name']
            app_id = AppsDescription.objects.get(id=app_name)
            current_form.app_id = app_name
            current_form.save()

            env_name = form.data['env_name']
            new_env_name = ''.join(env_name.split())

            env_id = InfraServiceInfo.objects.get(env_name=env_name).id
            request.session['app_name'] = app_name
            request.session['app_id'] = app_name
            request.session['env_id'] = env_id
            request.session['env_name'] = new_env_name
            request.session['ins_type'] = form.data['instance_type']
            request.session['env_desc'] = form.data['description']

            try:
                aws_home_folder_location = '/home/ec2-user/{ai}/{ei}/{en}'.format(ai=app_name,
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

            os.system('echo %s|sudo -S %s' % (None, 'sh /home/ec2-user/terraform-app.sh {} ec2'.format(aws_home_folder_location)))

            return HttpResponseRedirect(reverse("aws:infradb"))

    return render(request, "infraservice.html", {'form': form})




def infradatabase(request):

    form = InfraDatabase()

    if request.method == "POST":
        form = InfraDatabase(request.POST)

        if form.is_valid():
            current_form = form.save(commit=False)
            current_form.env_id = request.session['env_id']
            current_form.save()

            location = '/home/ec2-user/{ai}/{ei}/{en}'.format(ai=request.session['app_id'],
                                                             ei=request.session['env_id'],
                                                             en=request.session['env_name'])
            db_json(form.data['engine'], form.data['db_instance_class'],
                    form.data['volume_size'], form.data['username'],
                    form.data['password'], request.session['app_name'],
                    request.session['env_name'], request.session['env_id'],
                    location)

            os.system('echo %s|sudo -S %s' % (None, 'sh /home/ec2-user/terraform-app.sh {} rds'.format(location)))

            return HttpResponseRedirect(reverse("aws:infracicd"))

    else:
        form = InfraDatabase()

    return render(request, "infradatabase.html", {'form':form})



def infracicd(request):

    form = InfraCicds()

    if request.method == "POST":
        form = InfraCicds(request.POST)

        if form.is_valid():
            current_form = form.save(commit=False)
            current_form.app_id = request.session['app_id']
            current_form.save()
            location = '/home/ec2-user/{ai}/{ei}/{en}'.format(ai=request.session['app_id'],
                                                             ei=request.session['env_id'],
                                                             en=request.session['env_name'])
            cicd_json(request.session['app_name'], form.data['name'],
                      request.session['env_name'], request.session['env_id'],
                      form.data['name'], location)

            os.system('echo %s|sudo -S %s' % (None, 'sh /home/ec2-user/terraform-app.sh {} cicd'.format(location)))
            os.system('echo %s|sudo -S %s' % (None, 'sh /home/ec2-user/terraform-app.sh {} create'.format(location)))

            return HttpResponseRedirect(reverse("aws:manageenv"))

    else:
        form = InfraCicds()

    return render(request, "infracicd.html", {'form':form})



def createmigrations(request):

    form = CreateMigrationForm()

    if request.method == "POST":
        form = CreateMigrationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            ai = form.data['app_name']
            ei = form.data['env_name']
            en = InfraServiceInfo.objects.get(id=ei).env_name
            location = '/home/ec2-user/{ai}/{ei}/{en}'.format(ai=ai,
                                                              ei=ei,
                                                              en=en)
            dms_json(form.data['app_name'], en, ei, form.data['source_ip'],
                     '3306', form.data['source_username'],
                     form.data['source_password'], form.data['engine_name'], location)

            os.system('echo %s|sudo -S %s' % (None, 'sh terraform-app.sh {} dms'.format(location)))
            return HttpResponseRedirect(reverse('aws:managemigrations'))

    else:
        form = CreateMigrationForm()

    return render(request, "createmigrations.html", {'form':form})


def managemigrations(request):

    resp = CreateMigrations.objects.order_by("-id")
    return render(request, "managemigrations.html", {"migrate": resp})



def filter_env_names(request):

    appname = request.GET.get('appname', None)
    ap_id = AppsDescription.objects.get(id=appname)
    datas = InfraServiceInfo.objects.filter(app_name=ap_id).all()
    data = dict()
    for i in datas:
        data[i.id] = i.env_name
    print(data)
    request.session['appname'] = appname
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_rds_db(request):

    appname = request.GET.get('appname', None)
    app_name = request.session['appname']

    try:
        ai = AppsDescription.objects.get(name=app_name).id
        ei = InfraServiceInfo.objects.get(name=appname).id
        en = app_name

        location = '/home/ec2-user/{ai}/{ei}/{en}'.format(ai=ai,
                                                          ei=ei,
                                                          en=en)

        file_output_json = '/output.json'
        f3 = json.loads(open(location + file_output_json, "r").read())
        data = f3['RDS_Endpoint']['value']

    except:
        data = ''

    return HttpResponse(data, content_type='application/text')

def name_desc(request):

    appname = request.GET.get('appname', None)
    data = StaticData.objects.get(stack=appname).description
    return HttpResponse(data, content_type='application/text')