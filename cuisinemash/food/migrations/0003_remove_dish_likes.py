# Generated by Django 2.2.7 on 2021-02-08 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20210207_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='likes',
        ),
    ]
