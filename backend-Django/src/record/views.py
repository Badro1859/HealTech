from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from record.models import Lab, LabComponent, Medicine, Record, Problem, Allergie, Medication
from record.serializers import LabSerializer, LabComponentSerializer, \
        MedicineSerializer, RecordSerializer, \
        ProblemSerializer, AllergieSerializer, MedicationSerializer


class LabViewSet(ModelViewSet):
    serializer_class = LabSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Lab.objects.all()

class LabComponentViewSet(ModelViewSet):
    serializer_class = LabComponentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = LabComponent.objects.all()

class MedicineViewSet(ModelViewSet):
    serializer_class = MedicineSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Medicine.objects.all()


class RecordViewSet(ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Record.objects.all()
 
class ProblemViewSet(ModelViewSet):
    serializer_class = ProblemSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Problem.objects.all()

class AllergieViewSet(ModelViewSet):
    serializer_class = AllergieSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Allergie.objects.all()

class MedicationViewSet(ModelViewSet):
    serializer_class = MedicationSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Medication.objects.all()