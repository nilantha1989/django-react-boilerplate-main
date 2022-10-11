from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from  apps.appoinments.models import AppointmentAndAvailability

class AppointmentAndAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=AppointmentAndAvailability
        fields=['id','treatment_type','doctor_id','patient_id','prefered_pharmacy_id','is_booked','can_access_SCR','consult_copy_shared']


