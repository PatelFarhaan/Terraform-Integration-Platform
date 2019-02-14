# Generated by Django 2.1.5 on 2019-02-14 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0004_auto_20190214_1038'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cicd',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='app_name',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='env_name',
        ),
        migrations.DeleteModel(
            name='Ec2',
        ),
        migrations.DeleteModel(
            name='InfraCicd',
        ),
        migrations.DeleteModel(
            name='InfraDatabases',
        ),
        migrations.RemoveField(
            model_name='infraserviceinfo',
            name='app_name',
        ),
        migrations.DeleteModel(
            name='Rds',
        ),
        migrations.DeleteModel(
            name='ServerAwsInfo',
        ),
        migrations.DeleteModel(
            name='StaticData',
        ),
        migrations.DeleteModel(
            name='StaticData2',
        ),
        migrations.DeleteModel(
            name='AppsDescription',
        ),
        migrations.DeleteModel(
            name='CreateMigrations',
        ),
        migrations.DeleteModel(
            name='InfraServiceInfo',
        ),
    ]
