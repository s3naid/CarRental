from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import (
    DateTimeRangeField,
    RangeBoundary,
    RangeOperators,
)
from django.db import models

# Create your models here.

class Car(models.Model):
    car=models.CharField(max_length=50)
    seats=models.IntegerField()
    price_day=models.CharField(max_length=50)
    driver=models.BooleanField(default=False)


class Profile(CustomUser):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bonus=models.DecimalField(decimal_places=2)

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Booking(models.Model):
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='users')
    start_date=models.DateTimeField()
    end_date=models.DateTimeField(blank=True, null=True)
    cancelled = models.BooleanField(default=False)

    def clean(self):
        if self.start_date is None and self.start_date > self.end_date:
            raise ValidationError('Please enter proper date.')
        super(Booking, self).clean()