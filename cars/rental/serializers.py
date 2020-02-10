from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from accounts.serializers import UserCreateSerializer
from .models import Car,Booking,Profile
from accounts.models import CustomUser

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
    user=UserCreateSerializer()
    class Meta:
        model=Profile
        fields='__all__'
        read_only_fields = ['user', 'bonus']

    def create(self, validated_data):
        user_data=validated_data.pop('user')
        user_data['password']=make_password(user_data['password'])
        user = CustomUser.objects.create(**user_data)
        instance=Profile(user=user)
        print(instance)
        return instance