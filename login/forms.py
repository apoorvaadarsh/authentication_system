from cProfile import label
from django import forms
from signup.models import User

class ImagePicker(forms.ModelForm):
    class Meta:
        model=User
        fields=['profilePic']
        labels={'profilePic':''}
        # fields='__all__'
