# Generated by Django 3.0 on 2020-04-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200418_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='allstudent',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='studentphoto'),
        ),
    ]