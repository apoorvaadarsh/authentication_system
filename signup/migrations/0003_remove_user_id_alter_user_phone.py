# Generated by Django 4.0.3 on 2022-03-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_user_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
