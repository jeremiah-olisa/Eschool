# Generated by Django 2.2.9 on 2020-04-22 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200422_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='displayName',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]