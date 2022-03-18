from django.shortcuts import render
from signup.models import User
from .forms import ImagePicker

def login(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        user=User.objects.filter(phone=phone,password=password)
        print(user)
        if user: 
            return dashboard(request,user)
        else:
            return render(request,'error.html')
    return render(request,'login.html')

def dashboard(request,user):
    print(user[0],'details')
    if request.method=='POST':
        form=ImagePicker(request.POST,request.FILES)
        if form.is_valid():
           print(form ,'form')
           form.save()
           return render(request,'dashboard.html',{'form':form,'user':user[0]})
        else:
            return render('error.html')