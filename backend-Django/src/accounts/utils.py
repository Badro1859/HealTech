
from accounts.models import User
from accounts.serializers import UserSerializer



def get_or_create_user(data):
    
    ser = UserSerializer(data=data)
    if ser.is_valid(raise_exception=True):
        try:
            user = User.objects.filter(email=UserSerializer.validated_data['email'])
            return user
        except:
            return ser.save()

def update_user(instance, data):
    ser = UserSerializer(instance=instance, data=data, partial=True)
    
    if ser.is_valid(raise_exception=True):
        return ser.save()

