

from rest_framework import serializers

from record.models import Lab, LabComponent, Medicine, Record, Problem, Allergie, Medication



class LabSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lab
        fields = '__all__'
        read_only_fields = ('id',)

class LabComponentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LabComponent
        fields = '__all__'
        read_only_fields = ('id',)

class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ('id',)

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = '__all__'
        read_only_fields = ('id',)

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = '__all__'
        read_only_fields = ('id',)

class AllergieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Allergie
        fields = '__all__'
        read_only_fields = ('id',)

class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medication
        fields = '__all__'
        read_only_fields = ('id',)