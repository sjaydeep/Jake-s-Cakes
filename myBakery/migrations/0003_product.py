# Generated by Django 3.0.4 on 2020-04-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBakery', '0002_auto_20200407_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='static/img')),
            ],
        ),
    ]
