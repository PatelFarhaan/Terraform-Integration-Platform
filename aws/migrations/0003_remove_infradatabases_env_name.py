# Generated by Django 2.1.5 on 2019-02-06 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0002_auto_20190206_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infradatabases',
            name='env_name',
        ),
    ]
