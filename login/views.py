from django.shortcuts import render
from signup.models import User
from .forms import ImagePicker

def login(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        user=User.objects.filter(phone=phone,password=password)
        print(user,'if exists')
        if user:
            return dashboard(request,user[0])
        else:
            print('error page dispaly ')
            return render(request,'error.html')
    return render(request,'login.html')

def dashboard(request,user):
    print(user,'details')
    if request.method=='POST':
        form=ImagePicker(request.POST,request.FILES,instance=user)
        if(form.is_valid):
            form.save()
    form=ImagePicker(instance=user)
    return render(request,'dashboard.html',{'form':form,'user':user})