from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from .producer import publish
from .serializer import Registration, PatientRegistration
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets
from .models import Patient, Prescriptions
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def registrations (request):
    serializer = Registration(data=request.data)
    if serializer.is_valid():
        info = serializer.save()
        return Response({'username': info.username, 'email': info.email, 'id': info.id})
    else:
        raise (serializer.errors)


class PatientView(viewsets.ViewSet):
    def patient_reg (self, request):
        serializer = PatientRegistration(data=request.data)
        if serializer.is_valid():
            info = serializer.save()
            return Response ({'name': info.name, 'last_name': info.last_name, 'allergies': info.allergies})
        else:
            raise (serializer.errors)


    def patient_update (self, request, pk):
        patient = Patient.objects.filter(id=pk).first()
        info = request.data
        if not patient:
            raise ('user with this id does not exist')
        serializer = PatientRegistration(instance=patient, data=request.data, partial=True)
        if serializer.is_valid():
            info = serializer.save()
            return Response (f'{patient.name}s information has been updated')
        raise (serializer.errors)


    def patient_view (self, request, pk):
        patient = Patient.objects.filter(id=pk).first()
        if not patient:
            raise ('user with this id does not exist')
        serializer = PatientRegistration(patient)
        return Response (serializer.data)


    def patient_delete (self, request, pk):
        patient = Patient.objects.filter(id=pk).first()
        if not patient:
            raise (f'Patient with id {pk} does not exist')
        patient.delete()
        return Response (f'Patient with id {pk} has been deleted')



@api_view(['POST'])
@csrf_exempt
def prescription (request):
    info = request.data
    object = Prescriptions.objects.create(medicine_id=info['medicine_id'], patient_id=info['patient_id'], doctor_id=info['doctor_id'])
    new_object = Prescriptions.objects.select_related().filter(id=object.id).first()
    publish('prescription_fill', {'id': new_object.id, 'medicine': new_object.medicine.brand, 'patient_name': new_object.patient.name + ' ' + new_object.patient.last_name, 'doctor_id': new_object.doctor_id})
    return Response({'medicine': new_object.medicine.brand, 'name_last_name': f'{new_object.patient.name}  {new_object.patient.last_name}', 'doctor_id': new_object.doctor_id})



