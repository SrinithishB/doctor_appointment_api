from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorAvailabilityView, AppointmentCreateView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctors/<int:doctor_id>/availability/', DoctorAvailabilityView.as_view(), name='doctor-availability'),
    path('appointments/', AppointmentCreateView.as_view(), name='appointment-create'),
]
