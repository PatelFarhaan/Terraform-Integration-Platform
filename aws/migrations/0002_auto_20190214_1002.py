# Generated by Django 2.1.5 on 2019-02-14 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createmigrations',
            name='app_name',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='env_name',
        ),
    ]
