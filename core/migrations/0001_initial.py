# Generated by Django 3.0.6 on 2020-06-14 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('url', models.CharField(help_text='Link of the Page Error occured. Copy the link where the Error Occured from your browser address bar', max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('showDOB', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('showPhone', models.CharField(max_length=50)),
                ('fullName', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('disability', models.CharField(max_length=100)),
                ('displayImage_url', models.CharField(blank=True, max_length=500, null=True)),
                ('profile', models.TextField()),
                ('slug', models.SlugField()),
                ('displayName', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
