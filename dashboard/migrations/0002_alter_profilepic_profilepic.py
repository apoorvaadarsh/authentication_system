# Generated by Django 4.0.3 on 2022-03-20 21:30

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='profilePic',
            field=models.ImageField(upload_to=dashboard.models.profile_pic_path),
        ),
    ]