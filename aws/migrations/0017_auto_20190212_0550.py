# Generated by Django 2.1.5 on 2019-02-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0016_auto_20190212_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infraserviceinfo',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
