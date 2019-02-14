# Generated by Django 2.1.5 on 2019-02-14 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0007_appsdescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cicd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cicd_appname', models.CharField(max_length=1000)),
                ('repo_name', models.CharField(max_length=1000)),
                ('env_name', models.CharField(max_length=1000)),
                ('cicd_env_id', models.CharField(max_length=1000)),
                ('s3_artifact_bucket', models.CharField(max_length=1000)),
                ('cicd_artifact', models.CharField(blank=True, max_length=10000)),
                ('cicd_repo_http', models.CharField(blank=True, max_length=10000)),
                ('cicd_repo_ssh', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='CreateMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_db', models.CharField(blank=True, max_length=1000)),
                ('source_ip', models.GenericIPAddressField(default='192.168.1.2')),
                ('source_username', models.CharField(max_length=1000)),
                ('source_password', models.CharField(max_length=1000)),
                ('source_db', models.CharField(max_length=1000)),
                ('engine_name', models.CharField(blank=True, choices=[('MySQL', 'MySQL'), ('Oracle', 'Oracle')], max_length=1000)),
                ('app_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aws.AppsDescription')),
            ],
        ),
        migrations.CreateModel(
            name='Ec2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ec2_instancetype', models.CharField(max_length=1000)),
                ('ec2_count', models.CharField(max_length=1000)),
                ('ec2_ami', models.CharField(max_length=1000)),
                ('ec2_environment', models.CharField(max_length=1000)),
                ('ec2_appname', models.CharField(max_length=1000)),
                ('ec2_environment_id', models.CharField(max_length=1000)),
                ('ec2_public_dns', models.CharField(blank=True, max_length=10000)),
                ('ec2_dns', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='InfraCicd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_repo', models.CharField(choices=[('s3', 's3'), ('code commit', 'code commit')], max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('app_id', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfraDatabases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(choices=[('Oracle', 'Oracle'), ('MySQL', 'MySQL')], max_length=1000)),
                ('db_instance_class', models.CharField(choices=[('t2.micro', 't2.micro')], max_length=1000)),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=1000)),
                ('volume_size', models.PositiveIntegerField(default=0)),
                ('env_id', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfraServiceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env_name', models.CharField(max_length=1000, unique=True)),
                ('stack', models.CharField(choices=[("['ami-2']", "['ami-2']")], max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('no_of_instance', models.CharField(choices=[('1', '1'), ('2', '2'), ('4', '4')], max_length=256)),
                ('instance_type', models.CharField(choices=[('t2.micro', 't2.micro')], max_length=256)),
                ('ssh_location', models.GenericIPAddressField(default='192.168.1.2')),
                ('app_id', models.CharField(max_length=1000, null=True)),
                ('output_json_status', models.CharField(blank=True, default='In Progress', max_length=10000)),
                ('app_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aws.AppsDescription')),
            ],
        ),
        migrations.CreateModel(
            name='Rds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rds_engine', models.CharField(max_length=1000)),
                ('rds_instance', models.CharField(max_length=1000)),
                ('rds_storage', models.CharField(max_length=1000)),
                ('rds_username', models.CharField(max_length=1000)),
                ('rds_password', models.CharField(max_length=1000)),
                ('rds_appname', models.CharField(max_length=1000)),
                ('rds_environment', models.CharField(max_length=1000)),
                ('rds_environment_id', models.CharField(max_length=1000)),
                ('rds_database', models.CharField(blank=True, max_length=10000)),
                ('rds_endpoint', models.CharField(blank=True, max_length=10000)),
                ('rds_json_username', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ServerAwsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentId', models.CharField(max_length=1000)),
                ('configurationId', models.CharField(max_length=1000)),
                ('hostName', models.CharField(max_length=1000)),
                ('osName', models.CharField(max_length=1000)),
                ('osVersion', models.CharField(max_length=1000)),
                ('source', models.CharField(max_length=1000)),
                ('timeOfCreation', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='createmigrations',
            name='env_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aws.InfraServiceInfo'),
        ),
    ]
