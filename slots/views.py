from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ParkingSpot
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def home_page(request):
    return render(request, 'slots/home.html')

@login_required
def security_page(request):
    return render(request, 'registration/security.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('registration/security')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



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
