import datetime

from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trip,Station
from .serializer import TripSerializer

class TripList(APIView):
    def post(self,request):
        sttime = request.data["start_time_date"].split("-")
        trips = Trip.objects.filter(start_station = Station.objects.get(name=request.data["start_station"]),
                                    end_station = Station.objects.get(name=request.data["end_station"]),
                                    start_time_date__date = datetime.date(int(sttime[0]),int(sttime[1]),int(sttime[2])))
        serializer = TripSerializer(trips,many=True)
        return Response(serializer.data)
