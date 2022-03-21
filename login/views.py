from django.shortcuts import render
from dashboard.forms import ImagePicker
from dashboard.views import dashboard
from signup.models import User

def login(request):
    print(request , 'this is req')
    if request.method=='POST':
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        user=User.objects.filter(phone=phone,password=password)
        print(user,'if exists')
        if user:
            form=ImagePicker(request.POST,request.FILES,initial={'phone':phone})
            return dashboard(request,user[0])
        else:
            print('error page dispaly ')
            return render(request,'error.html')
    return render(request,'login.html')