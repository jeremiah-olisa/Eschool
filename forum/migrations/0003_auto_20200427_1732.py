# Generated by Django 2.2.3 on 2020-04-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200427_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='user',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
    ]
