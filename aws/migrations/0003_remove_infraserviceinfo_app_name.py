# Generated by Django 2.1.5 on 2019-02-14 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0002_auto_20190214_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infraserviceinfo',
            name='app_name',
        ),
    ]
