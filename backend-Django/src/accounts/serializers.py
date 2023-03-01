from django.db import IntegrityError, transaction
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


from accounts.models import User, Admin




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        read_only_fields = ('id',)


    def create(self, validated_data):
        try:
            user = User.objects._create_user(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def update(self, instance, validated_data):
        print(validated_data)
        password = validated_data.pop('password')

        user = super().update(instance, validated_data)

        user.set_password(password)
        user.save()

        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        ret.pop('password')
        return ret

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        read_only_fields = ('id', 'role')

class PasswordResetSerializer(serializers.Serializer):
    """
    A serializer that lets a user change set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    new_password1 = serializers.CharField(required=True)

    new_password2 = serializers.CharField(required=True)


    def is_valid(self, raise_exception):
        super().is_valid(raise_exception=True)

        if self.validated_data['new_password1'] != self.validated_data['new_password2']:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )

        return True


    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        password = self.validated_data["new_password1"]
        self.instance.set_password(password)

        self.instance.save()

        return self.instance


class AdminSerializer(serializers.ModelSerializer):

    user = UserUpdateSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = [
            'id',
            'user',
            'first_name', 
            'last_name', 
            'gender', 
            'date_of_birth', 
            'phone',
            'address',
            'profile_picture'
        ]

        read_only_field = ('id')

class DoctorSerializer(serializers.ModelSerializer):
    # TODO
    pass

class EmployeeSerializer(serializers.ModelSerializer):
    # TODO
    pass

class PatientSerializer(serializers.ModelSerializer):
    # TODO
    pass