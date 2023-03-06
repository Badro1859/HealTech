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

from rest_framework.renderers import StaticHTMLRenderer

## local packages

from accounts.models import User, Admin, Service, Doctor, Employee, Patient, Hospital
from accounts.serializers import \
    UserSerializer, AdminSerializer, \
    PasswordResetSerializer, ServiceSerializer, HospitalSerializer, \
    DoctorSerializer, EmployeeSerializer, PatientSerializer
from accounts.utils import get_userSerializer, get_userUpdateSerializer, get_instance_by_username

from accounts.permissions import IsOwnerOrAdmin, IsCustomAdmin, IsAdminOrReadOnly


class Profile(APIView):

    def get(self, request):
        model = apps.get_model(app_label='accounts', model_name=request.user.role)
        instance = model.objects.filter(user=request.user)

        if len(instance) == 0:
            return Response({'Error':'this user does not exist!!'}, status=status.HTTP_400_BAD_REQUEST)

        instance = instance[0]
        if request.user.role == 'Admin':
            return Response(AdminSerializer(instance=instance).data, status=status.HTTP_200_OK)
        if request.user.role == 'Doctor':
            return Response(DoctorSerializer(instance=instance).data, status=status.HTTP_200_OK)
        if request.user.role == 'Employee':
            return Response(EmployeeSerializer(instance=instance).data, status=status.HTTP_200_OK)
        
        return Response(PatientSerializer(instance=instance).data, status=status.HTTP_200_OK)


class CustomModelViewSet(ModelViewSet):

    ## global params
    permission_classes = (IsAuthenticated, )


    ## API methods


    @action(detail=True, renderer_classes=[StaticHTMLRenderer], methods=['post'])
    def reset_password(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.user
        serializer = PasswordResetSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"success": "Password reset successful"},
                        status=status.HTTP_201_CREATED,)



    ### GET method (all)
    def list(self, request):
        return super().list(request)


    ### GET method (pk)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    ### POST method
    def create(self, request, *args, **kwargs):
        self.userSerializer = get_userSerializer(data=request.data)#.get('user'))
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


class AdminViewSet(CustomModelViewSet):

    ## global params
    serializer_class = AdminSerializer
    # permission_classes = (IsAdminUser, )

    queryset = Admin.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append(IsCustomAdmin())
        return permissions


class DoctorViewSet(CustomModelViewSet):

    ## global params
    serializer_class = DoctorSerializer

    ## for 'get' params
    queryset = Doctor.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append(IsOwnerOrAdmin())
        permissions.append(IsAdminUser())
        return permissions


class EmployeeViewSet(CustomModelViewSet):
    ## global params
    serializer_class = EmployeeSerializer

    ## for 'get' params
    queryset = Employee.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append(IsOwnerOrAdmin())
        permissions.append(IsAdminUser())
        return permissions


class PatientViewSet(CustomModelViewSet):
    ## global params
    serializer_class = PatientSerializer

    ## for 'get' params
    queryset = Patient.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append(IsOwnerOrAdmin())
        return permissions


class ServiceViewSet(ModelViewSet):

    serializer_class = ServiceSerializer

    queryset = Service.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append(IsAdminOrReadOnly())
        return permissions


class HospitalAPIView(APIView):

    permission_classes = (IsAdminOrReadOnly, )

    def get_object(self):
        hospital = Hospital.objects.all()
        if len(hospital) == 0 :
            hos = Hospital(name="hospital name").save()
            return hos
        return hospital[0]

    def get(self, request):
        ser = HospitalSerializer(self.get_object())
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = HospitalSerializer(self.get_object(), data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_205_RESET_CONTENT)
