from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=CustomUser
        fields='__all__'
