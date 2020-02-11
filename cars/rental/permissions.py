from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Booking

class UserProfilePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user and request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj.user == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj.user == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False

class IsUpdateProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        print(view.kwargs)
        try:
            booking = Booking.objects.get(pk=view.kwargs['pk'])
        except:
            return False
        if request.user.profile.id == booking.user_id:
            return True
        return False