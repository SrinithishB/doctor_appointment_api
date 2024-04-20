from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Doctor, WeeklySchedule, Appointment
from .serializer import DoctorSerializer, WeeklyScheduleSerializer, AppointmentSerializer

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'pk'

class DoctorAvailabilityView(generics.RetrieveAPIView):
    serializer_class = WeeklyScheduleSerializer

    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return WeeklySchedule.objects.filter(doctor_id=doctor_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(day_of_week=self.request.GET.get('day_of_week'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
