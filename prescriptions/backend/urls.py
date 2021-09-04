from django.conf import settings
from django.urls import path, include
from .views import registrations, PatientView, prescription
urlpatterns = [
    path('register/', registrations),
    path('patient', PatientView.as_view({
        'post': 'patient_reg'
    })),
    path('patient/<str:pk>', PatientView.as_view(
        {
            'get': 'patient_view',
            'patch': 'patient_update',
            'delete': 'patient_delete'
        }
    )),
    path('prescription/', prescription)
]

if settings.DEBUG:
    print('aloha brother')
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
