

from rest_framework import serializers
from rest_framework.fields import (  # NOQA # isort:skip
    CreateOnlyDefault, CurrentUserDefault, SkipField, empty
)

from appointment.models import Appointment
from accounts.serializers import DoctorSerializer, PatientSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.ReadOnlyField(source='doctor.full_name')
    patient_name = serializers.ReadOnlyField(source='patient.full_name')

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ('id', 'service', 'employee')
