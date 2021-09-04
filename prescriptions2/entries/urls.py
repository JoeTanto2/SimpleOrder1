from django.urls import path, include
from .views import prescriptions, pick_up

urlpatterns = [
    path('admin/', prescriptions),
    path('all/', prescriptions),
    path('pick-up/<str:pk>', pick_up),
]
