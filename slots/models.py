from django.db import models



class ParkingSpot(models.Model):
    SPOT_STATUS = (
        ('available', 'Available'),
        ('closed', 'Closed'),
        ('unavailable', 'Unavailable'),
    )
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=20, choices=SPOT_STATUS, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
