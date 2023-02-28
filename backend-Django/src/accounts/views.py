from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.


from accounts.models import User, Admin
from accounts.serializers import UserSerializer, AdminSerializer
from accounts.utils import get_or_create_user, update_user




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
        self.user = get_or_create_user(data=request.data)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.user)

    ### PUT method
    def update(self, request, *args, **kwargs):

        ## updata the user instance
        admin = self.get_object()
        update_user(admin.user, request.data)

        ## updata admin instance
        return super().update(request, *args, **kwargs)

    ### DELETE method
    def destroy(self, request, *args, **kwargs):
        ## delete only the user instance (on cascade)
        instance = self.get_object()
        self.perform_destroy(instance.user)

        return Response(status=status.HTTP_204_NO_CONTENT)


