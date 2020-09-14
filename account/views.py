from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import auth
from urllib import request

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        Password1=request.POST['Password1']
        Password2=request.POST['Password2']

        if Password1==Password2:
            if User.objects.filter(username=username).exists():
                return render(request,'account/register.html',{'error':'Username is already taken'})
            else :
                if User.objects.filter(email=email).exists():
                    return render(request,'account/register.html',{'error':'email is already taken'})
                else:
                    user=User.objects.create_user(first_name=request.POST['first_name'],last_name=request.POST['last_name'],username=request.POST['username'],email=request.POST['email'],password=request.POST['Password1'])
                    auth.login(request,user)
                    user.save()
                    return redirect('login')
        else:
            return render(request,'account/register.html',{'error':'Password does not match'})
    else:
        #user
        return render(request,'account/register.html')



def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['Password1'])
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
             return render(request,'account/login.html',{'error':'Username or password is incorrect'})
    else:  
        return render(request,'account/login.html')


def dashboard(request):
    return render(request,'account/dashboard.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request) 
        return redirect('home')