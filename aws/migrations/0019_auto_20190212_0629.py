# Generated by Django 2.1.5 on 2019-02-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0018_auto_20190212_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmigrations',
            name='env_name',
            field=models.CharField(choices=[(None, None)], max_length=1000),
        ),
    ]
