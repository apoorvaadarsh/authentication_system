# Generated by Django 4.0.3 on 2022-03-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adress',
            field=models.TextField(default='NULL'),
        ),
    ]