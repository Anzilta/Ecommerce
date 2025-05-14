from django.db import models
from django.contrib.auth.models import AbstractUser

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
