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


    datas = InfraServiceInfo.objects.filter(app_name='first_app').all()
    data = list()
    for i in datas:
        data.append(i.env_name)
    print(data)


if __name__ == '__main__':
    # populate_Seed_data()
    query()