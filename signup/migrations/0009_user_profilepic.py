# Generated by Django 4.0.3 on 2022-03-20 21:44

from django.db import migrations, models
import signup.models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_remove_user_profilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(default='NULL', upload_to=signup.models.profile_pic_path, verbose_name='Profile Pic'),
        ),
    ]
