# Generated by Django 3.0.6 on 2020-06-16 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='displayImage_url',
        ),
    ]
