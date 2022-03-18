# Generated by Django 4.0.3 on 2022-03-18 08:13

from django.db import migrations, models
import signup.models
import tkinter


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_alter_user_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(default='NULL', upload_to=signup.models.profile_pic_path, verbose_name=tkinter.Image),
        ),
    ]
