# Generated by Django 3.2 on 2021-05-02 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruteforce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='bruteforce/profile_pics'),
        ),
    ]