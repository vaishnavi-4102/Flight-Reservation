from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length = 20)
    operating_airline = models.CharField(max_length= 25)
    departure_city = models.CharField(max_length= 25)
    arrival_city = models.CharField(max_length= 25)
    date_of_departure = models.DateField(max_length= 25)
    estimated_time_of_departure = models.TimeField()


class Passenger(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 20,blank=True, null = True)
    phone_no = models.CharField(max_length=10)

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete = models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete = models.CASCADE)