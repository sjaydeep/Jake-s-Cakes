# Generated by Django 3.0.4 on 2020-04-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBakery', '0018_auto_20200415_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image_width',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics'),
        ),
    ]
