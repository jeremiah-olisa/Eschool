# Generated by Django 2.2.9 on 2020-04-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='material',
            field=models.FileField(blank=True, null=True, upload_to='class-material/'),
        ),
        migrations.AlterField(
            model_name='class',
            name='subject',
            field=models.CharField(choices=[('agric', 'agric'), ('biology', 'biology'), ('civic', 'civic'), ('english', 'english'), ('math', 'math'), ('ccp', 'ccp'), ('dp', 'dp'), ('economics', 'economics'), ('ict', 'ict'), ('accts', 'accts'), ('chemistry', 'chemistry'), ('commerce', 'commerce'), ('fisheries', 'fisheries'), ('f-math', 'f-math'), ('f-nut', 'f-nut'), ('government', 'government'), ('literature', 'literature'), ('physics', 'physics')], max_length=100),
        ),
    ]