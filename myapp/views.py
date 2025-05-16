from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Userdetails ,product_details,CartItem
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.http import HttpResponse

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
            mail= user_obj.email
            print(user_obj)
        except User.DoesNotExist: 
            messages.error(request,"no user with that email")
            return render(request, './login.html')   
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if mail=='anzilasd@gmail.com':
              return redirect('admin_dashboard')
            else :
                return redirect('home1')
        else :
            messages.error(request,"invalid password") 
    return render(request, './login.html')
def home_view(request):
    return render(request,"./home.html")
def home1_view(request):
    return render(request,"./home1.html")
# def admin_view(request):
#     return render(request,"admin_home.html")
def dashboard_view(request):
    users=Userdetails.objects.all()
    products=product_details.objects.all()
    context={
       'users':users,
       "products":products,
         }
    return render(request,"./admin_dashboard.html",context)

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
        # password=request.POST.get('password')

        user.username=username
        user.place=place
        user.age=age
        user.phoneNumber=phoneNumber
        user.email=email
        # user.password=password
        user.save()

        return redirect("profile")
    return render(request,'update_user.html',{'user':user}) 

def delete_user(request , email):
    user=get_object_or_404(Userdetails,email=email)
    user.delete()
    return redirect('admin_dashboard')

def delete_product(request, product_id):
    product=get_object_or_404(product_details,id=product_id)
    product.delete()
    return redirect("admin_dashboard")

def profile_view(request):
    return render( request,'./profile.html')

def homeproduct_view(request):
    products=product_details.objects.all()
    context={
        'products':products,
    }
    return render(request,"./homeproducts.html",context)
 


def addproduct_view(request):
    if request.method=='POST':
        product_name=request.POST.get("product_name")
        type=request.POST.get('type')
        weight=request.POST.get('weight')
        price=request.POST.get('price')
        stock=request.POST.get('stock')
        image=request.FILES.get('image')
        if stock and int(stock) > 0:
            is_available = True
        else:
            is_available = False

        product=product_details.objects.create(product_name=product_name,type=type,weight=weight,price=price,stock=stock,image=image, is_available = is_available)
        product.save()
        return redirect('products') 
    return render  (request,"./add_product.html")
def product_view(request):
    products=product_details.objects.all()
    context={
        'products':products,
    }
    return render(request,"./products.html",context)

def addtocart_view(request , product_id):
    product=get_object_or_404(product_details,id=product_id)
    user=request.user

    cart_items,created=CartItem.objects.get_or_create(user=user,product=product)

    if not created:
        cart_items.quantity+=1
        cart_items.save()

    return redirect('cart')

def cart_view(request):
    cart_items=CartItem.objects.filter(user=request.user)
    total =sum(item.subtotal() for item in cart_items)

    return render(request,"./cart.html",{'cart_items':cart_items,'total':total})
def updatecart(request , item_id):
    item=get_object_or_404(CartItem,id=item_id,user=request.user)
    action=request.POST.get('action')

    if action=='increment':
       item.quantity +=1
    elif action=='decrement' and item.quantity>1:
        item.quantity-=1
    item.save()
    return redirect('cart')
def deletecartitem(request,item_id):
    item=get_object_or_404(CartItem,id=item_id,user=request.user)
    item.delete()
    return redirect('cart')
        
# def clear_cart(request):
#     request.session['cart'] = {}
#     return HttpResponse("Cart cleared.")
def logout_view(request):
   
    logout(request)
    return redirect("login")  
