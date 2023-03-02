
from accounts.models import User
from accounts.serializers import UserSerializer, UserUpdateSerializer

from django.apps import apps

def get_userSerializer(data): 
    ser = UserSerializer(data=data)
    if ser.is_valid(raise_exception=True):
        return ser
    return None

def get_userUpdateSerializer(instance, data): 
    ser = UserUpdateSerializer(instance=instance, data=data, partial=True)
    if ser.is_valid(raise_exception=True):
        return ser
    return None

def get_instance_by_username(username):
    user = User.objects.filter(username=username)
    return apps.get_model(app_label='accounts', model_name=user[0].role).objects.filter(user=user)[0]
