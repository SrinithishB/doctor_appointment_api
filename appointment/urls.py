from django.urls import path
from .views import DoctorListView, DoctorDetailView, doctor_availability, AppointmentCreateView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('appointments/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('doctors/<int:doctor_id>/availability/', doctor_availability, name='doctor-availability'),
]
