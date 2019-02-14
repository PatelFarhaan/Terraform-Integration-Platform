# Generated by Django 2.1.5 on 2019-02-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0006_staticdata_staticdata2'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppsDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField()),
                ('plan_to_migrate', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], max_length=256)),
                ('server_names', models.TextField(null=True)),
                ('create_app_response', models.TextField(null=True)),
            ],
        ),
    ]
