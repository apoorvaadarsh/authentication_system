from django.shortcuts import render

from dashboard.forms import ImagePicker

# Create your views here.

def dashboard(request,user):
    if(request.method=='POST'):
        form=ImagePicker(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return render(request,'dashboard.html',{'form':form,'user':user})
        form=ImagePicker()
    return render(request, 'dashboard.html', {'form': form,'user':user})