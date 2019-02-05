import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws_config.settings')

import django
django.setup()

####################################################################################


from aws.models import StaticData, AppsDescription, InfraServiceInfo


def populate_Seed_data():

    StaticData.objects.all().delete()

    stack_list = ['ami-03787fa0594b1f151', 'PHP', 'Lnux']
    stack_description = ['testing1', 'testing2', 'testing3']

    instance_type = ['t2.micro']
    engine = ['Oracle', 'MySQL']
    instance_number = [1,2,4]


    StaticData.objects.create(stack=stack_list,
                              description=stack_description,
                              instance_type=instance_type,
                              instance_number=instance_number)


def test_db():

    obj = AppsDescription.objects.get(name='Aifi-2')
    print(obj.id)

    # import ipdb; ipdb.set_trace()
    VIEW_STACK_CHOICES = []

    ins_choice = StaticData.objects.all()
    for i in ins_choice:
        print(i.stack)
        print(i.instance_number)
        print(i.instance_number)

if __name__ == '__main__':
    populate_Seed_data()
    # test_db()
    # print("Success!!!")