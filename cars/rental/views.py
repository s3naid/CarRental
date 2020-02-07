from django.shortcuts import render
from rest_framework import filters

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .permissions import IsOwner

from .serializers import ProfileSerializer,CarSerializer,BookingSerializer
from .models import Profile,Car,Booking

class CarViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'delete', 'update']:
            self.permission_classes = [IsAdminUser]
        return super(self.__class__, self).get_permissions()

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
