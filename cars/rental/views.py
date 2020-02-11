from datetime import datetime
from rest_framework import filters, viewsets

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .permissions import UserProfilePermission, IsUpdateProfile

from .serializers import ProfileSerializer,CarSerializer,BookingSerializer
from .models import Profile,Car,Booking

class CarViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'delete', 'update']:
            self.permission_classes = [IsAdminUser]
        return super(self.__class__, self).get_permissions()

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [UserProfilePermission]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    # def check_bonus(self,request):
    #     profile=Profile.objects.get(pk=self.request.user.id)
    #     now = datetime.now()
    #     date = datetime.strptime(self.request.data['end_date'], '%Y-%m-%d %H:%M:%S')
    #     print (self.request.data)
    #     if now > date:
    #         profile.bonus=profile.bonus+1
    #         profile.save()

    def get_permissions(self):
        if self.action in ['update']:
            self.permission_classes = [IsUpdateProfile]
        return super(self.__class__, self).get_permissions()


    def perform_create(self, serializer):
        # self.check_bonus(self.request)
        return serializer.save(user=self.request.user.profile)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.profile)
