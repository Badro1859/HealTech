
from django.urls import path

from rest_framework.routers import DefaultRouter


from appointment.views import AppointmentAPIView



routes = DefaultRouter() ## associated all : list, create, retrieve, update, destroy

# ## router create all associated url (post -> create, get -> list ...)
routes.register(r'appointment', AppointmentAPIView,  basename='appointment')

app_name='appointment'
urlpatterns = [
    *routes.urls,
   
]
