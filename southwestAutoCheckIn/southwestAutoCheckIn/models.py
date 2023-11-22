from django.db import models

class FlightReservation(models.Model):
    confirmation_code = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    flight_time = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.confirmation_code}"
