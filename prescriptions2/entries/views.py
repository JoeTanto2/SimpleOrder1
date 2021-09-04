from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OurPrescriptions
from .serializer import PrescriptionSerializer
from django.core import serializers
from .producer import publish

@api_view(['GET'])
def prescriptions (request):
    objects = OurPrescriptions.objects.all()
    serializer = PrescriptionSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pick_up (request, pk):
    publish('pickup', pk)
    return Response('thank you for your pickup')