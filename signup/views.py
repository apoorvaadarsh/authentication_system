from django.shortcuts import render
import mysql.connector as sql

name=''
phone=''
password=''
adress=''

def signup(request):
    global name,phone,password,adress
    if request.method=='POST':
        m=sql.connect(host='localhost',user='root',password='2410',database='authentication_system')
        cursor=m.cursor()
        data=request.POST
        for key,value in data.items():
            if key=='name':
                name=value
            elif key=='phone':
                phone=value
            elif key=='password':
                password=value
            elif key=='adress':
                adress=value
        c="insert into users Values('{}','{}','{}','{}')".format(name,password,adress,phone)
        cursor.execute(c)
        m.commit()
    return render(request,'signup.html')