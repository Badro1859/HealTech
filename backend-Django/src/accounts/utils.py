
from accounts.models import User
from accounts.serializers import UserSerializer, UserUpdateSerializer



def get_userSerializer(data): 
    ser = UserSerializer(data=data)
    if ser.is_valid(raise_exception=True):
        return ser
    return None

def get_userUpdateSerializer(instance, data): 
    ser = UserUpdateSerializer(instance=instance, data=data)
    if ser.is_valid(raise_exception=True):
        return ser
    return None
