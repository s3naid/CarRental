from django.urls import include, path
from .views import ProfileViewSet

urlpatterns = [
    path(r'profile/', iProfileViewSet),
]