# Generated by Django 3.2.4 on 2021-06-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_objects', '0005_merge_0004_auto_20210626_1312_0004_auto_20210626_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museumobject',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/object_images/'),
        ),
        migrations.AlterField(
            model_name='museumobject',
            name='model3d',
            field=models.FileField(blank=True, upload_to='static/object_3dmodels/'),
        ),
    ]
