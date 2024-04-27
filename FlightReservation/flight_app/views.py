from django.shortcuts import render
from .models import Flight,Passenger,Reservation
from .serializer import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here

@api_view(['POST'])
def find_flights(request):
    flights = flights.objects.filter(departure_city = request.data.get('departure_city'), arrival_city = request.data.get('arrival_city'), date_of_departure=request.data.get('date_of_departure'))
    serializer = FlightSerializer(flights, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flight'])

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.last_name = request.data['last_name']
    passenger.email = request.data['email']
    passenger.phone_no = request.data['phone_no']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)

    



class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer