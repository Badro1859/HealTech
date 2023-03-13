

from rest_framework import serializers

from record.models import Lab, LabComponent, Medicine, Record



class LabSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lab
        read_only_fields = ('id',)

class LabComponentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LabComponent
        read_only_fields = ('id',)


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record