from django.shortcuts import render 
from apps.appoinments.models import AppointmentAndAvailability
from apps.appoinments.serializers import AppointmentAndAvailabilitySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from django.http import Http404

class AppointmentAndAvailabilityList(APIView):

    def get(self,request):
        appoinments=AppointmentAndAvailability.objects.all()
        serializer=AppointmentAndAvailabilitySerializer(appoinments,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=AppointmentAndAvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AppointmentAndAvailabilityDetail(APIView):
    def get_object(self,pk):
        try:
            return AppointmentAndAvailability.objects.get(pk=pk)
        except AppointmentAndAvailability.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        appoinments=self.get_object(pk)
        serializer=AppointmentAndAvailabilitySerializer(appoinments)
        return Response(serializer.data)

    def put(self,request,pk):
        appoinments=self.get_object(pk)
        serializer=AppointmentAndAvailabilitySerializer(appoinments,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        student=self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentAndAvailabilityCustom(APIView):
    def get_objects(self,filter_param):
        try:
            return AppointmentAndAvailability.objects.filter(is_booked=filter_param)
        except AppointmentAndAvailability.DoesNotExist:
            raise Http404
    
    def get(self,request):
        appoinments=self.get_objects("False")
        serializer=AppointmentAndAvailabilitySerializer(appoinments,many=True)
        return Response(serializer.data)



