import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws_config.settings')

import django
django.setup()

####################################################################################


from aws.models import StaticData, AppsDescription, InfraServiceInfo, Ec2


def populate_Seed_data():

    StaticData.objects.all().delete()

    stack_list = ['ami-03787fa0594b1f151']
    stack_description = ['PHP and LINUX']

    instance_type = ['t2.micro']
    engine = ['Oracle', 'MySQL']
    instance_number = [1,2,4]


    StaticData.objects.create(stack=stack_list,
                              description=stack_description,
                              instance_type=instance_type,
                              instance_number=instance_number,
                              engine=engine)


def query():

    # kv_dict = {}
    # app_names_list = []
    # app_names = AppsDescription.objects.all()
    # for i in app_names:
    #     app_names_list.append(i.name)
    #
    # for k in app_names_list:
    #     datas = InfraServiceInfo.objects.filter(app_name=k).all()
    #     data = list()
    #     for v in datas:
    #         data.append(v.env_name)
    #
    #     kv_dict[k] = data

    env_names = []
    app_names = AppsDescription.objects.all()
    app_name_list = []
    for i in app_names:
        app_name_list.append(i.name)
    for j in app_name_list:
        data = InfraServiceInfo.objects.filter(app_name=j).all()
        for v in data:
            env_names.append(v.env_name)

    VIEW_ENV_CHOICES = []
    for names in env_names:
        VIEW_ENV_CHOICES.append(('{}'.format(names), '{}'.format(names)), )

    print(VIEW_ENV_CHOICES)

if __name__ == '__main__':
    # populate_Seed_data()
    query()