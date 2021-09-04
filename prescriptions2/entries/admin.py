from django.contrib import admin
from .models import OurPrescriptions, PickedUpPrescriptions
admin.site.register(OurPrescriptions)
admin.site.register(PickedUpPrescriptions)