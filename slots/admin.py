from django.contrib import admin
from .models import ParkingSpot

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'vehicle_type', 'latitude', 'longitude', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'vehicle_type']
    search_fields = ['name', 'number']
    ordering = ('number',)
