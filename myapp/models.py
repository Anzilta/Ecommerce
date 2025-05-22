from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Userdetails(AbstractUser):
    age = models.IntegerField(default=15, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, default="0000000000", blank=True)
    place = models.CharField(max_length=255, default='Unknown', blank=True)

    def __str__(self):
        return self.username
class product_details(models.Model):
    product_name=models.CharField(max_length=100)
    type=models.CharField(max_length=50)
    weight=models.IntegerField(max_length=10)
    price=models.DecimalField(max_digits=10 ,decimal_places=2)
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='product/')
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
class CartItem(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey('product_details' ,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


    def subtotal(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.product.product_name} x {self.quantity}"
    
class OrderDetails(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    totalprice=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return f"order #{self.id} by {self.user.username}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(OrderDetails, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # snapshot price at order time

    def subtotal(self):
        return self.quantity * self.price


class History(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    totalprice=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return f"order #{self.id} by {self.user.username}"

class HistoryItem(models.Model):
    history = models.ForeignKey(History, related_name='history_items', on_delete=models.CASCADE)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price