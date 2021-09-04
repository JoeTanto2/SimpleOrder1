from django.contrib import admin
from .models import Doctor, Medicine, Patient, Prescriptions

admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Patient)
admin.site.register(Prescriptions)