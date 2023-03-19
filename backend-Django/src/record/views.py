from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from accounts.models import Patient
from record.models import Lab, LabComponent, Medicine, Record, Problem, Allergie, Medication, Test, Exam, PlanOfCare
from record.serializers import LabSerializer, LabComponentSerializer, \
        MedicineSerializer, RecordSerializer, \
        ProblemSerializer, AllergieSerializer, MedicationSerializer, \
        TestSerializer, ExamSerializer, PlanOfCareSerializer


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


class RecordViewSet(ViewSet, CreateAPIView):
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Record.objects.all()
    
    def get_serialized_record(self, instance):
        instance['problems'] = ProblemSerializer(Problem.objects.filter(record=instance['id']), many=True).data
        instance['allergies'] = AllergieSerializer(Allergie.objects.filter(record=instance['id']), many=True).data
        instance['medications'] = MedicationSerializer(Medication.objects.filter(record=instance['id']), many=True).data
        instance['planOfCares'] = PlanOfCareSerializer(PlanOfCare.objects.filter(record=instance['id']), many=True).data
        instance['exams'] = ExamSerializer(Exam.objects.filter(record=instance['id']), many=True).data
        # instance['labs'] = ExamSerializer(Exam.objects.filter(record=instance['id']), many=True).data

        return instance

    def list(self, request):
        # return records by patient id
        if not request.data.get('patient'):
            return Response({'error': 'please give me patient ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        patient = Patient.objects.filter(pk=request.data.get('patient'))
        if len(patient) != 1:
            return Response({'error': 'please give me valid patient ID'}, status=status.HTTP_400_BAD_REQUEST)

        # get all record and its params
        records = Record.objects.filter(patient=self.request.data.get('patient'))
        serialzer = RecordSerializer(instance=records, many=True)

        for item in serialzer.data:
            item = self.get_serialized_record(item)

        return Response(serialzer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecordSerializer(instance=instance, many=False)
        data = self.get_serialized_record(serializer.data)
        return Response(data, status=status.HTTP_200_OK)

    def get_labs(self, components):
        labs = {}
        for item in components:
            cp = LabComponent.objects.filter(pk=item['component'])
            if len(cp) == 0:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                labs[str(cp.lab)].append(item)
            except:
                labs[str(cp.lab)] = []
                labs[str(cp.lab)].append(item)
