from django.db import models

from django.db import models

class OurPrescriptions (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)
    medicine = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    doctor_id = models.IntegerField()

    def __str__(self):
        return self.patient_name + '+' + self.medicine

class PickedUpPrescriptions (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)
    medicine = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    doctor_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name + '+' + self.medicine