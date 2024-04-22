from django.shortcuts import render

# Create your views here.
import datetime
from rest_framework import generics
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def doctor_availability(request, doctor_id):
    # day_of_week = request.GET.get('day_of_week')
    # day_of_week = datetime.datetime.today().strftime('%A')
    queryset = WeeklySchedule.objects.filter(doctor_id=doctor_id)
    serializer = WeeklyScheduleSerializer(queryset, many=True)
    return Response(serializer.data)

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
