from django.shortcuts import render
from signup.models import User

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        adress=request.POST.get('adress')
        user=User(name=name,phone=phone,password=password,adress=adress)
        user.save()
        print("data written")
    return render(request,'signup.html')