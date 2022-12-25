import datetime

from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trip,Station,Ticket
from .serializer import TripSerializer,TicketSerializer

class TripList(APIView):
    def post(self,request):
        sttime = request.data["start_time_date"].split("-")
        trips = Trip.objects.filter(start_station = Station.objects.get(name=request.data["start_station"]),
                                    end_station = Station.objects.get(name=request.data["end_station"]),
                                    start_time_date__date = datetime.date(int(sttime[0]),int(sttime[1]),int(sttime[2])))
        serializer = TripSerializer(trips,many=True)
        return Response({"trips":serializer.data})

class TripBook(APIView):
    def post(self,request):
        if not Ticket.objects.get(trip_id = request.data["trip_id"], passenger_id = request.data["passenger_id"]):
            mytrip=Trip.objects.get(id=request.data["trip_id"])
            total=mytrip.train.total_capacity
            if mytrip.remaining_capacity == -1:
                mytrip.remaining_capacity = mytrip.train.total_capacity
            remaining=mytrip.remaining_capacity
            seatnum=total-remaining+1
            ticketid=request.data["trip_id"]+str(seatnum)
            myticket = Ticket(trip_id=request.data["trip_id"],passenger_id=request.data["passenger_id"],seat_number=seatnum,number=ticketid,user=request.user)
            myticket.save()
            mytrip.remaining_capacity -= 1
            mytrip.save(update_fields=["remaining_capacity"])
            serializer = TicketSerializer(myticket)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"message":"is exist"},status=status.HTTP_400_BAD_REQUEST)

class TravelsList(APIView):
    def get(self,request):
        tickets = Ticket.objects.filter(user=request.user)
        serializer = TicketSerializer(tickets, many=True)
        return Response({"tickets":serializer.data})


class TripDetail(APIView):
    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return Response(serializer.data)