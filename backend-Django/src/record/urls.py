from django.urls import path

from rest_framework.routers import DefaultRouter

from record import views


routes = DefaultRouter()

routes.register(r'lab', views.LabViewSet, basename='lab')
routes.register(r'lab_component', views.LabComponentViewSet, basename='lab-component')
routes.register(r'medicine', views.MedicineViewSet, basename='medicine')
routes.register(r'record', views.RecordViewSet, basename='record')

app_name='record'
urlpatterns = [
    *routes.urls,
]
