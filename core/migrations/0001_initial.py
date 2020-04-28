# Generated by Django 2.2.9 on 2020-04-22 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('dob', models.DateTimeField()),
                ('role', models.CharField(choices=[('Student', 'primary'), ('Teacher', 'success'), ('Parent', 'info'), ('Mere-User', 'light')], max_length=50)),
                ('grade', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
                ('showdob', models.BooleanField(default=False)),
                ('fullName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('disability', models.CharField(max_length=100)),
                ('profile', models.TextField()),
                ('slug', models.SlugField()),
                ('displayImage', models.ImageField(upload_to='')),
            ],
        ),
    ]
