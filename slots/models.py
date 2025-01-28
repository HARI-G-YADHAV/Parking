from django.db import models



class ParkingSpot(models.Model):
    SPOT_STATUS = (
        ('available', 'Available'),
        ('closed', 'Closed'),
        ('unavailable', 'Unavailable'),
    )
    VEHICLE_TYPE = (
        ('car', 'Car'),
        ('bike', 'Bike'),
    )
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=20, choices=SPOT_STATUS, default='available')
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle_type.title()} - {self.name}"
    
