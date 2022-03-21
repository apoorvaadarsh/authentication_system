from cProfile import label
from django import forms
from dashboard.models import ProfilePic

class ImagePicker(forms.ModelForm):
    class Meta:
        model = ProfilePic
        fields =['profilePic']
        label={'profilePic':''}
