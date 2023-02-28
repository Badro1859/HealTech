
from django.urls import path, include

from rest_framework.routers import SimpleRouter, DefaultRouter
from djoser.views import TokenCreateView, TokenDestroyView
from accounts import views


# routes = SimpleRouter() ## associated only : list and detail

routes = DefaultRouter() ## associated all : list, create, retrieve, update, destroy

## router create all associated url (post -> create, get -> list ...)
routes.register(r'admin', views.AdminViewSet,  basename='admin')



app_name='accounts'
urlpatterns = [
    *routes.urls,

    path(r"login", TokenCreateView.as_view(), name="login"),
    path(r"logout", TokenDestroyView.as_view(), name="logout"),

]
