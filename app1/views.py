
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from app1.models import useraccount_tbl,user_tbl,seller_tbl,staff_tbl
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request,'index.html')
    # return render(request,'staff.html')
def create(request):
    return render(request,'createaccount.html')
def createacc(request):
    a=User()
    b=useraccount_tbl()
    u=user_tbl()
    a.first_name=request.POST.get('firstname')
    a.username=request.POST.get('username')
    password=request.POST.get('password')
    a.set_password(password)
    a.email=request.POST.get('email')
    
    b.username=request.POST.get('username')
    b.firstname=request.POST.get('firstname')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phone')
    b.accounttype="user"
   
    u.username=request.POST.get('username')
    u.firstname=request.POST.get('firstname')
    u.lastname=request.POST.get('lastname')
    u.gender=request.POST.get('gender')
    u.email=request.POST.get('email')
    u.phone=request.POST.get('phone')
    u.district=request.POST.get('district')
    u.address=request.POST.get('address')
    u.photo=request.POST.get('photo')
    c=request.FILES['photo']
    fs=FileSystemStorage()
    d=fs.save(c.name,c)
    fileurl=fs.url(d)
    u.photo=fileurl
   
    a.save()
    b.save()
    u.save()
    return redirect('/')
def login(request):
    return render(request,'login.html')
def user(request):
    return render(request,'user.html')
def login1(request):
    uname=request.POST.get('username')
    pwd=request.POST.get('password')
    data=authenticate(username=uname,password=pwd)
    request.session['username']=uname
    if data is not None and data.is_superuser==1:
        return redirect('/admin1/')
    elif data is not None and data.is_superuser==0:
        return redirect('/user1/')
    else:
        return HttpResponse('invaliduser')
def adduser(request):
    u=user_tbl()
    u.username=request.POST.get('username')
    u.firstname=request.POST.get('firstname')
    u.lastname=request.POST.get('lastname')
    u.gender=request.POST.get('gender')
    u.email=request.POST.get('email')
    u.phone=request.POST.get('phone')
    u.district=request.POST.get('district')
    u.address=request.POST.get('address')
    u.photo=request.POST.get('photo')
    c=request.FILES['photo']
    fs=FileSystemStorage()
    d=fs.save(c.name,c)
    fileurl=fs.url(d)
    u.photo=fileurl
    u.save()
    return redirect('/')
def addseller(request):
    s=seller_tbl()
    s.username=request.POST.get('username')
    s.firstname=request.POST.get('firstname')
    s.lastname=request.POST.get('lastname')
    s.gender=request.POST.get('gender')
    s.email=request.POST.get('email')
    s.phone=request.POST.get('phone')
    s.district=request.POST.get('district')
    s.address=request.POST.get('address')
    s.photo=request.POST.get('photo')
    c=request.FILES['photo']
    fs=FileSystemStorage()
    d=fs.save(c.name,c)
    fileurl=fs.url(d)
    s.photo=fileurl
    s.save()
    return redirect('/')
def addstaff(request):
    st=staff_tbl()
    st.username=request.POST.get('username')
    st.firstname=request.POST.get('firstname')
    st.lastname=request.POST.get('lastname')
    st.gender=request.POST.get('gender')
    st.age=request.POST.get('age')
    st.designation=request.POST.get('designation')
    st.email=request.POST.get('email')
    st.phone=request.POST.get('phone')
    st.district=request.POST.get('district')
    st.address=request.POST.get('address')
    st.photo=request.POST.get('photo')
    c=request.FILES['photo']
    fs=FileSystemStorage()
    d=fs.save(c.name,c)
    fileurl=fs.url(d)
    st.photo=fileurl
    st.save()
    return redirect('/')
def admin1(request):
    return render(request,'admin.html')
def user1(request):
    return render(request,'user.html')









# Create your views here.
