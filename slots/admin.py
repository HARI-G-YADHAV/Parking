from django.contrib import admin
from .models import ParkingSpot

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['name']
    ordering = ('id',)
