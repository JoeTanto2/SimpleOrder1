from rest_framework import serializers
from .models import OurPrescriptions, PickedUpPrescriptions
class PrescriptionSerializer (serializers.ModelSerializer):
    class Meta:
        model = OurPrescriptions
        fields = '__all__'

class PikUpSerializer (serializers.ModelSerializer):
    class Meta:
        model = PickedUpPrescriptions
        fields = '__all__'

