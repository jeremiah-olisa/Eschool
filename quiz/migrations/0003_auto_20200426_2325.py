# Generated by Django 2.2.3 on 2020-04-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200426_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='url',
            field=models.SlugField(help_text='a user friendly url preferablly the name of your test after removing whitespace e.g Test 101 => Test-101', max_length=60, verbose_name='user friendly url'),
        ),
    ]