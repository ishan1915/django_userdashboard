from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings




# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to='profilephotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s details"


class CustomUser(AbstractUser):  
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)