from django.shortcuts import render
import mysql.connector as sql

phone=''
password=''

def login(request):
    global phone,password
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',password='2410',database='authentication_system')
        cursor=m.cursor()
        data=request.POST
        for key,value in data.items():
            if key=='phone':
                phone=value
            else:
                password=value
        c="select * from users where password='{}' and phone='{}'".format(password,phone)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if(t==()):
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
    return render(request,'login.html')