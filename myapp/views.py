from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Userdetails
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User


def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        place=request.POST.get('place')
        age=request.POST.get('age')
        phoneNumber=request.POST.get('phoneNumber')
        email=request.POST.get('email')
        password=request.POST.get('password')
      
# chech for email is exist
        if Userdetails.objects.filter(email=email).exists():
            messages.error(request,'email alredy exists')
        else:
            user=Userdetails.objects.create_user(username=username,email=email,password=password)
            user.place=place
            user.age=age
            user.phoneNumber=phoneNumber
            user.save()
            messages.success(request,'account created successfully')
            return redirect('login')
        

    return render(request,'./signup.html')
def login_view(request):
    if request.method=='POST':

        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user_obj = Userdetails.objects.get(email=email)
            username = user_obj.username
            print(user_obj)
        except User.DoesNotExist: 
            messages.error(request,"no user with that email")
            return render(request, './login.html')   
        user= authenticate(request,username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('home')
        else :
            messages.error(request,"invalid password") 
    return render(request, './login.html')
def home_view(request):
    return render(request,"./home.html")