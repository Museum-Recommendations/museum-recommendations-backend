# Generated by Django 3.2.4 on 2021-06-27 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_score', '0002_auto_20210626_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreview',
            name='user',
        ),
    ]
