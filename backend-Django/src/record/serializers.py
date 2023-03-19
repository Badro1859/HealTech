

from rest_framework import serializers

from record.models import Lab, LabComponent, Medicine, Record, Problem, Allergie, Medication, Test, Exam, PlanOfCare



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


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        exclude = ['id', 'record']

class AllergieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergie
        exclude = ['id', 'record']

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        exclude = ['id', 'record']

class PlanOfCareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanOfCare
        exclude = ['id', 'record']

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        exclude = ['id', 'record']

class TestSerializer(serializers.ModelSerializer):
    component_info = LabComponentSerializer(read_only=True)
    class Meta:
        model = Test
        exclude = ['id', 'record']

class RecordSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True, required=False)
    allergies = AllergieSerializer(many=True, required=False)
    medications = MedicationSerializer(many=True, required=False)
    planOfCares = PlanOfCareSerializer(many=True, required=False)
    exams = ExamSerializer(many=True, required=False)
    tests = TestSerializer(many=True, required=False)

    doctor_name = serializers.ReadOnlyField(source='doctor.full_name')
    patient_name = serializers.ReadOnlyField(source='patient.full_name')
    class Meta:
        model = Record
        fields = [
            'id', 'doctor', 'patient', 'doctor_name', 'patient_name',
            'title', 'date', 'abstract',
            'problems', 'allergies', 'medications', 'planOfCares', 'exams', 'tests'
        ]
        read_only_fields = ('id',)


    def create(self, validated_data):
        problems = validated_data.pop('problems', [])
        allergies = validated_data.pop('allergies', [])
        medications = validated_data.pop('medications', [])
        planOfCares = validated_data.pop('planOfCares', [])
        exams = validated_data.pop('exams', [])
        tests = validated_data.pop('tests', [])

        instance = super().create(validated_data)

        for item in problems:
            Problem.objects.create(record=instance, **item)
        for item in allergies:
            Allergie.objects.create(record=instance, **item)
        for item in medications:
            Medication.objects.create(record=instance, **item)
        for item in planOfCares:
            PlanOfCare.objects.create(record=instance, **item)
        for item in exams:
            Exam.objects.create(record=instance, **item)

        return instance










