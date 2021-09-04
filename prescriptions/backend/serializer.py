from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Medicine

class Registration (serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PatientRegistration (serializers.ModelSerializer):
    allergies = serializers.JSONField(required=False)
    class Meta:
        model = Patient
        fields = '__all__'

class MedicineSerializer (serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
