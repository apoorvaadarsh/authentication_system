from django.db import models
from signup.models import User

def profile_pic_path(profile,filename):
    print('profile is : ', profile,filename)
    print('phone is : ', profile.phone)
    return '{0}/{1}'.format(profile.phone,filename)

# Create your models here.
class ProfilePic(models.Model):
    phone=models.CharField(max_length=10,primary_key=True)
    profilePic=models.ImageField(upload_to=profile_pic_path)
