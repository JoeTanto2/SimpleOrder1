from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Medicine (models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField(null=False)
    dose = models.IntegerField(null=False)

    def __str__(self):
        return self.brand

class Doctor (models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    license_id = models.CharField(max_length=50)

    def __str__(self):
        return self.license_id

class Patient (models.Model):
    name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    age = models.IntegerField(default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.CharField(max_length=15)
    weight = models.IntegerField()
    allergies = models.JSONField(default=None, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Prescriptions (models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.patient.last_name} + {self.medicine.brand}'