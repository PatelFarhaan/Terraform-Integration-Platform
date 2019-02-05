import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws_config.settings')

import django
django.setup()

####################################################################################


from aws.models import StaticData


def populate_Seed_data():

    StaticData.objects.all().delete()

    stack_list = ['ami-03787fa0594b1f151 PHP and Lnux']
    stack_description = ['testing']

    instance_type = ['t2.micro']
    engine = ['Oracle', 'MySQL']
    instance_number = [1,2,4]


    StaticData.objects.create(stack=stack_list,
                              description=stack_description)

    StaticData.objects.create(instance_type=instance_type)

    StaticData.objects.create(instance_number=instance_number)


def test_db():
    obj = StaticData.objects.all()

if __name__ == '__main__':
    populate_Seed_data()
    # test_db()
    # print("Success!!!")