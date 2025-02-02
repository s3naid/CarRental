from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.hashers import make_password
from accounts.serializers import UserCreateSerializer
from .models import Car,Booking,Profile
from accounts.models import CustomUser
from django.utils import timezone
from datetime import datetime

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    bonus = serializers.SerializerMethodField()

    class Meta:
        model=Booking
        fields=['car', 'start_date', 'end_date', 'bonus']
        read_only_fields = ['user', 'cancelled','bonus']

    def get_bonus(self, obj: Booking):
        bookings=Booking.objects.filter(
                                        user_id=obj.user_id,
                                        end_date__lt=timezone.now()
        ).count()
        print(bookings)
        profile = Profile.objects.get(pk=obj.user.id)
        profile.bonus=bookings
        profile.save()
        return (bookings)

    def validate(self, data):
        #ubaciti provjeru da je start_date veci od trenutnog (timezone.now() ne radi)
        if data['start_date'] > data['end_date']:
              raise serializers.ValidationError("End date must be after start date.")
        return data

    def create(self, validated_data):
        #date ranges overlap if (StartDate1 <= EndDate2) and (EndDate1 >= StartDate2)
        bookings=Booking.objects.filter(
                                    car__pk=validated_data['car'].id,
                                    start_date__lte=validated_data['end_date'],
                                    end_date__gte=validated_data['start_date'],
        )
        if bookings:
            raise serializers.ValidationError("This car is unavaible for selected dates. Please choose different car.")

        instance = Booking.objects.create(**validated_data)
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    user=UserCreateSerializer()
    class Meta:
        model=Profile
        fields=['phone','user','bonus']
        read_only_fields = ['user', 'bonus']

    #Nested serializer mora imati create metodu
    def create(self, validated_data):
        user_data=validated_data.pop('user')
        user_data['password']=make_password(user_data['password'])
        user = CustomUser.objects.create(**user_data)
        instance=Profile(user=user, **validated_data)
        return instance