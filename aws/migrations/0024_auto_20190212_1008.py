# Generated by Django 2.1.5 on 2019-02-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0023_auto_20190212_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmigrations',
            name='env_name',
            field=models.CharField(blank=True, choices=[('first_env', 'first_env'), ('farhaan2', 'farhaan2'), ('aifi-test3', 'aifi-test3'), ('second', 'second'), ('aifi', 'aifi'), ('aifi1', 'aifi1'), ('testing-phase', 'testing-phase'), ('xzxczxc', 'xzxczxc')], max_length=1000),
        ),
    ]