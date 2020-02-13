from django.db import models
from accounts.models import CustomUser


# Create your models here.

class Car(models.Model):
    car=models.CharField(max_length=50)
    seats=models.IntegerField()
    price_day=models.CharField(max_length=50)
    driver=models.BooleanField(default=False)

    def __str__(self):
        return self.car

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bonus=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    phone=models.IntegerField(null=True)

class Booking(models.Model):
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='users')
    start_date=models.DateTimeField()
    end_date=models.DateTimeField(blank=True, null=True)

