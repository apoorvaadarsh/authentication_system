# Generated by Django 4.0.3 on 2022-03-20 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_alter_user_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profilePic',
        ),
    ]
