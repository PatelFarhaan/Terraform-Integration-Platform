import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aws_config.settings')

import django
django.setup()

####################################################################################


from aws.models import StaticData, StaticData2


def populate_Seed_data():

    StaticData2.objects.all().delete()


    stack_list = ['ami-2']
    stack_description = ['test']

    instance_type = ['t2.micro']
    engine = ['Oracle', 'MySQL']
    instance_number = [1,2,4]

    StaticData2.objects.create(instance_type=instance_type,
                              instance_number=instance_number,
                              engine=engine)
    StaticData.objects.create(stack=stack_list,
                              description=stack_description)


def query():

    ins_choice = StaticData.objects.get(stack='ami-1-test')
    print(ins_choice.description)





if __name__ == '__main__':
    populate_Seed_data()
    # query()