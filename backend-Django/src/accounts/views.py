from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.


from accounts.models import User, Admin
from accounts.serializers import UserSerializer, AdminSerializer, PasswordResetSerializer
from accounts.utils import get_userSerializer, get_userUpdateSerializer


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

class AdminViewSet(ModelViewSet):

    ## global params
    serializer_class = AdminSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [TokenAuthentication, ]

    # http_method_names = ['post']

    ## for 'get' params
    queryset = Admin.objects.all()

    

    ## API methods

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
        admin = self.get_object()
        self.userSerializer = get_userUpdateSerializer(instance=admin.user, data=request.data)

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

class DoctorViewSet(ModelViewSet):
    # TODO 
    pass

class EmployeeViewSet(ModelViewSet):
    # TODO 
    pass

class PatientViewSet(ModelViewSet):
    # TODO 
    pass