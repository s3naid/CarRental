from rest_framework import serializers

from .models import Car,Booking,Profile

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['car', 'start_date', 'end_date']
        read_only_fields = ['user']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        read_only_fields = ['user', 'bonus']
