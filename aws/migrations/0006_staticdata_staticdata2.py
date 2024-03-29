# Generated by Django 2.1.5 on 2019-02-14 11:07

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aws', '0005_auto_20190214_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stack', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StaticData2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_type', django_mysql.models.ListCharField(models.CharField(max_length=1000), max_length=1000, size=None)),
                ('instance_number', django_mysql.models.ListCharField(models.CharField(max_length=1000), max_length=1000, size=None)),
                ('engine', django_mysql.models.ListCharField(models.CharField(max_length=1000), max_length=1000, size=None)),
            ],
        ),
    ]
