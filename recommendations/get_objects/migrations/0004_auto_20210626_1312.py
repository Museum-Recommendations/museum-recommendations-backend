# Generated by Django 3.2.4 on 2021-06-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_objects', '0003_rename_name_museumobject_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='museumobject',
            name='photo',
        ),
        migrations.AddField(
            model_name='museumobject',
            name='image',
            field=models.ImageField(blank=True, upload_to='object_images/'),
        ),
        migrations.AlterField(
            model_name='museumobject',
            name='model3d',
            field=models.FileField(blank=True, upload_to='object_3dmodels/'),
        ),
    ]
