# Generated by Django 2.1.5 on 2019-01-31 15:46

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0004_example_app_names'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Example',
        ),
        migrations.RenameField(
            model_name='appsdescription',
            old_name='desc',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='appsdescription',
            name='configuration',
        ),
        migrations.RemoveField(
            model_name='appsdescription',
            name='migrate',
        ),
        migrations.AddField(
            model_name='appsdescription',
            name='app_names',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('appdemo', 'appdemo'), ('demosms', 'demosms'), ('tets', 'tets')], default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appsdescription',
            name='plan_to_migrate',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default=None, max_length=256),
            preserve_default=False,
        ),
    ]
