from rest_framework import serializers
import re
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flight_number(request,flight_number):
        print("validate_flightNumber")
        if(re.match("^[a-zA-Z0-9]*$", flight_number)== None):
            raise serializers.ValidationError("Invalid Flight Number, Enter it correctly")
        return flight_number
    
    # For checking all data types
    
    # def validate(self, data):
    #  print("validate")
    #  print (data)
    #  return data 


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

