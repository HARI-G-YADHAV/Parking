from django.db import models

# Create your models here.
class Slot(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'Available', 'Available'
        UNAVAILABLE = 'Unavailable', 'Unavailable'
        CLOSED = 'Closed', 'Closed'
    class Vehicle(models.TextChoices):
        CAR = 'Car', 'Car'
        BIKE = 'Bike', 'Bike'
    slot_id = models.AutoField(primary_key=True)
    slot_name = models.CharField(max_length=255, null=False)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
        null=False
    )
    vehicles = models.CharField(
        max_length=20,
        choices=Vehicle.choices,
        default=Vehicle.CAR,
        null=False
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slot_name
    
