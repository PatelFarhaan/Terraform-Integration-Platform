# Generated by Django 2.1.5 on 2019-02-07 10:15

from django.db import migrations, models


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
            name='destination_db',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='env_name',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='source_db',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='source_ip',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='source_password',
        ),
        migrations.RemoveField(
            model_name='createmigrations',
            name='source_username',
        ),
        migrations.AddField(
            model_name='infraserviceinfo',
            name='app_id',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]