from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)


    REQUIRED_FIELDS = ['first_name', 'last_name']
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD='email'