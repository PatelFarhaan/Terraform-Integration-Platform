# Generated by Django 2.1.5 on 2019-02-04 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0016_author_books_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.RemoveField(
            model_name='library',
            name='author',
        ),
        migrations.RemoveField(
            model_name='library',
            name='books',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]