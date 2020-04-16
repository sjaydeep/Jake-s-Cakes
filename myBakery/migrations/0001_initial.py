# Generated by Django 3.0.4 on 2020-04-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('phone', models.BigIntegerField(max_length=10)),
                ('desc', models.TextField(max_length=2000)),
                ('date', models.DateField()),
            ],
        ),
    ]
