from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
# Create your models here.
from accounts.models import Patient, Doctor, Employee, Service



class Appointment(models.Model):
    status_choices = (
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
        ("Pending", "Pending"),
        ("Expired", "Expired"),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)

    date = models.DateField(_("appointment date"), default=timezone.now().date())
    time = models.TimeField(_("appointment time"), default=timezone.now().time())

    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, blank=True, null=True, on_delete=models.DO_NOTHING)
        
    status = models.CharField(_("status"), max_length=20, choices=status_choices, default="Pending")

    doctor_notes = models.TextField(_("medical notes"), blank=True, null=True, help_text="Signs  & Symptoms.")
    patient_notes = models.TextField(_("your message"), help_text="Please, describe your problem.", blank=True, null=True)

    def __str__(self):
        return f"{self.id}. {self.patient.user.username} {self.date}"

    class Meta:
        verbose_name_plural = "Appointments"
        ordering = ("-date", "-time")
