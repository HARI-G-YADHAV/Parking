from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ParkingSpot

# Create your views here.
def home_page(request):
    return render(request, 'slots/home.html')

@login_required
def security_page(request):
    return render(request, 'slots/security.html')

def get_parking_spots(request):
    # API endpoint to get parking spots data
    spots = ParkingSpot.objects.all()
    data = [{
        'id': spot.id,
        'lat': spot.latitude,
        'lng': spot.longitude,
        'name': spot.name,
        'status': spot.status,
        'number': spot.number
    } for spot in spots]
    return JsonResponse(data, safe=False)

def parking_spots_api(request):
    vehicle_type = request.GET.get('vehicle_type')
    spots = ParkingSpot.objects.all()
    
    if vehicle_type:
        spots = spots.filter(vehicle_type=vehicle_type)
    
    spots_data = [{
        'number': spot.number,
        'name': spot.name,
        'lat': spot.latitude,
        'lng': spot.longitude,
        'status': spot.status,
        'vehicle_type': spot.vehicle_type
    } for spot in spots]
    
    return JsonResponse(spots_data, safe=False)

def home(request):
    return render(request, 'slots/home.html')

def front(request):
    return render(request, 'slots/front.html')
