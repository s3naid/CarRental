from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    phone=models.IntegerField()
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD='email'