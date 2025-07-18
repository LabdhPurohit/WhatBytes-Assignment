from rest_framework.routers import DefaultRouter
from .views import PatientDoctorMappingViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', PatientDoctorMappingViewSet, basename='mapping')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', PatientDoctorMappingViewSet.as_view({'get': 'doctors_for_patient'}), name='doctors-for-patient'),
] 