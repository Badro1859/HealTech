from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
from accounts.models import Doctor, Patient



class Medicine(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Lab(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(_("available"), default=True)
    description = models.TextField(_("description"), blank=True, null=True)

    def __str__(self):
        return self.name
    
class LabComponent(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    low = models.CharField(max_length=5)
    high = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name



class Record(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    title = models.CharField(max_length=300)
    date = models.DateField()
    abstract = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title


class Problem(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    observation = models.TextField()
    status = models.TextField()


class Allergie(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    reaction = models.CharField(max_length=200)
    severity = models.CharField(max_length=200)


class Medication(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    dose = models.CharField(max_length=20)
    notes = models.TextField(_("prescription guidelines"), blank=True, null=True)
    duration = models.CharField(_("duration"), max_length=57, blank=True, null=True)


class Test(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    component = models.ForeignKey(LabComponent, on_delete=models.CASCADE)

    result = models.CharField(max_length=20)


class Exam(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    conclusion = models.TextField()
    result = models.FileField(upload_to='test_result/', blank=True, null=True)


class PlanOfCare(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    activity_name = models.TextField()
    planned_date = models.DateField()
    instructions = models.TextField()