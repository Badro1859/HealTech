
from rest_framework import serializers


from accounts.models import User, Admin




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        read_only_field = ('id')


    def create(self, validated_data):
        return super().create(validated_data)


class AdminSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = [
            'user',
            'first_name', 
            'last_name', 
            'gender', 
            'date_of_birth', 
            'phone',
            'address',
            'profile_picture'
        ]


