# Generated by Django 2.2.1 on 2020-06-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published_date',
            new_name='pub_date',
        ),
    ]