# Generated by Django 2.1.5 on 2019-02-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0013_auto_20190209_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsdescription',
            name='plan_to_migrate',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], max_length=256),
        ),
        migrations.AlterField(
            model_name='createmigrations',
            name='env_name',
            field=models.CharField(choices=[('first_env', 'first_env'), ('farhaan2', 'farhaan2'), ('second', 'second'), ('aifi', 'aifi'), ('aifi1', 'aifi1'), ('aifi-test3', 'aifi-test3'), ('testing-phase', 'testing-phase'), ('xzxczxc', 'xzxczxc')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='infraserviceinfo',
            name='output_json_status',
            field=models.CharField(blank=True, default='In Progress', max_length=10000),
        ),
    ]