from django.db import models
from django.contrib.auth.models import AbstractUser

class Userdetails(AbstractUser):
    age = models.IntegerField(default=15, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, default="0000000000", blank=True)
    place = models.CharField(max_length=255, default='Unknown', blank=True)

    def __str__(self):
        return self.username
