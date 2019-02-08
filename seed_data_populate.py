import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws_config.settings')

import django
django.setup()

####################################################################################


from aws.models import StaticData, AppsDescription, InfraServiceInfo


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

    # obj = AppsDescription.objects.get(name='first_app')
    # print(obj.id)
    #
    # # obj2 = InfraServiceInfo.objects.filter(app_id=id).all()
    # # for j in obj2:
    # #     print(j.description)

    obj = InfraServiceInfo.objects.order_by('-id')
    for i in obj:
        print(i.ssh_location)

if __name__ == '__main__':
    # populate_Seed_data()
    query()