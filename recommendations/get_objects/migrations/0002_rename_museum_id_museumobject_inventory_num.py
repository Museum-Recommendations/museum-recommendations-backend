# Generated by Django 3.2.4 on 2021-06-26 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_objects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museumobject',
            old_name='museum_id',
            new_name='inventory_num',
        ),
    ]
