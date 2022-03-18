from tkinter import Image
from django.db import models

# Create your models here.

def profile_pic_path(user,filename):
    print(user,filename)
    return '{0}/{1}'.format(user.phone,filename)

class User(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10,primary_key=True)
    password=models.CharField(max_length=50)
    adress=models.TextField(default="NULL")
    profilePic=models.ImageField(upload_to=profile_pic_path,default="NULL",verbose_name="Profile Pic")
