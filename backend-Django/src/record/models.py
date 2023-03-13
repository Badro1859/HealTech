from django.db import models

# Create your models here.



class Record(models.Model):

    doctor = models.ForeignKey(to, on_delete)
    patient = models.ForeignKey(to, on_delete)

    title = models.CharField(max_length=300)
    date = models.DateField()
    abstract = models.TextField()
    
    def __str__(self):
        return self.title
    




class Lab(mdoels.Model):
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
    

class Test(models.Model):

    record = models.ForeignKey(Record, on_delete=models.CASCAD)
    component = models.ForeignKey(LabComponent, on_delete=models.CASCADE)

    result = models.CharField(max_length=20)



class Problem(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    observation = models.TextField()
    status = models.TextField()

class PlanOfCare(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    activity_name = models.TextField()
    planned_date = models.DateField()
    instructions = models.TextField()


class Medicine(medels.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Medication(models.Model):
    
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    dose = models.CharField(max_length=20)
    notes = models.TextField(_("prescription guidelines"), blank=True, null=True)
    duration = models.CharField(_("duration"), max_length=57, blank=True, null=True)




class Allergie(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    reaction = models.CharField(max_length=200)
    severity = models.CharField(max_length=200)
    

class Exam(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    conclusion = models.TextField()
    result = models.FileField(upload_to='test_result/', blank=True, null=True)