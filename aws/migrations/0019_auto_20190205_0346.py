# Generated by Django 2.1.5 on 2019-02-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0018_auto_20190205_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infraserviceinfo',
            name='description',
            field=models.TextField(choices=[('', ''), ('testing', 'Testing'), ('', ''), ('testing', 'testing'), ('testing', 'testing')], editable=False),
        ),
    ]