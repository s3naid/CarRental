from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet, CarViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'cars', CarViewSet)
router.register(r'booking', BookingViewSet)
urlpatterns = router.urls