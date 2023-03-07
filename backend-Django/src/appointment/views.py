from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from accounts.models import Patient, Doctor, Employee
from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer

class AppointmentAPIView(ViewSet, ListCreateAPIView, RetrieveUpdateAPIView):

    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated, )


    def get_queryset(self):
        if self.request.user.role == 'Patient':
            patient = Patient.objects.filter(user=self.request.user)[0]
            return Appointment.objects.filter(patient=patient)
        if self.request.user.role == 'Doctor':
            doctor = Doctor.objects.filter(user=self.request.user)[0]
            return Appointment.objects.filter(doctor=doctor)
        if self.request.user.role == 'Employee':
            emp = Employee.objects.filter(user=self.request.user)[0]
            return Appointment.objects.filter(service=emp.in_service)

        return Appointment.objects.all()
    



    ## GET methods for all appointments
    def list(self, request):
        return super().list(request)

    ## POST methods
    def create(self, request):
        return super().create(request)

    def perform_create(self, serializer):
        emp = Employee.objects.filter(user=self.request.user)[0]
        serializer.save(service=emp.in_service, employee=emp)



    ## GET methods for one appointment <pk>
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    ## PUT method
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    ## PATCH method
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


    
    def get_permissions(self):

        permissions = super().get_permissions()

        if self.request.method.lower() != 'get':
            permissions.append(IsAdminUser())
        
        return permissions