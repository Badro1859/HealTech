from django.shortcuts import render
from django.apps import apps

## rest framework packages

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


## local packages

from accounts.models import User, Admin, Service, Doctor, Employee, Patient
from accounts.serializers import \
    UserSerializer, AdminSerializer, \
    PasswordResetSerializer, ServiceSerializer, \
    DoctorSerializer, EmployeeSerializer, PatientSerializer
from accounts.utils import get_userSerializer, get_userUpdateSerializer, get_instance_by_username

from accounts.permissions import IsOwnerOrAdmin


class CustomModelViewSet(ModelViewSet):

    ## global params
    # permission_classes = (IsOwnerOrAdmin,)


    ## API methods

    ## ^/profile  GET method
    @action(detail=False)
    def profile(self, request):
        if not request.user.is_authenticated :
            return Response({'error':'you are not a user!! please login'}, status=status.HTTP_204_NO_CONTENT)
        
        model = apps.get_model(app_label='accounts', model_name=request.user.role)
        instance = model.objects.filter(user=request.user)

        if len(instance) == 0:
            return Response({'Error':'this user does not exist!!'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(instance[0])
        return Response(serializer.data, status=status.HTTP_200_OK)

    ### GET method (all)
    def list(self, request):
        return super().list(request)


    ### GET method (pk)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    ### POST method
    def create(self, request, *args, **kwargs):
        self.userSerializer = get_userSerializer(data=request.data.get('user'))
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.userSerializer.save()
        serializer.save(user=user)

    ### PUT method
    def update(self, request, *args, **kwargs):

        ## updata the user instance
        instance = self.get_object()
        self.userSerializer = get_userUpdateSerializer(instance=instance.user, data=request.data.get('user'))

        ## updata admin instance
        return super().update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        updated_user = self.userSerializer.save()

        serializer.save(user=updated_user)

    ### DELETE method
    def destroy(self, request, *args, **kwargs):
        ## delete only the user instance (on cascade)
        instance = self.get_object()
        self.perform_destroy(instance.user)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ResetPasswordAPIView(UpdateAPIView):
    
    permission_classes = (AllowAny,)
    
    queryset = Admin.objects.all()
    serializer_class = PasswordResetSerializer

    def get_object(self):
        admin = super().get_object()
        
        return admin.user
    

    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({"success": "Password reset successful"},
                        status=status.HTTP_201_CREATED,)


class AdminViewSet(CustomModelViewSet):

    ## global params
    serializer_class = AdminSerializer
    # permission_classes = (IsAdminUser, )

    queryset = Admin.objects.all()


class DoctorViewSet(CustomModelViewSet):

    ## global params
    serializer_class = DoctorSerializer

    ## for 'get' params
    queryset = Doctor.objects.all()


class EmployeeViewSet(CustomModelViewSet):
    ## global params
    serializer_class = EmployeeSerializer

    ## for 'get' params
    queryset = Employee.objects.all()


class PatientViewSet(CustomModelViewSet):
    ## global params
    serializer_class = PatientSerializer

    ## for 'get' params
    queryset = Patient.objects.all()


class ServiceViewSet(ModelViewSet):

    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [TokenAuthentication, ]

    queryset = Service.objects.all()