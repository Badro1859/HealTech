

from rest_framework import serializers


from appointment.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ('id', 'service', 'employee')
