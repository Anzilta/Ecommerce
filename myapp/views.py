from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Userdetails
from django.contrib.auth import login,authenticate,logout
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
def add_product(request):
    return render(request,"add_product.html")
def admin_view(request):
    return render(request,"admin_home.html")

def edit_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user=request.user

    if request.method=='POST':
        username=request.POST.get('username')
        place=request.POST.get('place')
        age=request.POST.get('age')
        phoneNumber=request.POST.get('phoneNumber')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user.username=username
        user.place=place
        user.age=age
        user.phoneNumeber=phoneNumber
        user.email=email
        user.password=password
        user.save()

        return redirect("home")
    return render(request,'update_user.html',{'user':user}) 
def logout_view(request):
    logout(request)
    return redirect("login")   