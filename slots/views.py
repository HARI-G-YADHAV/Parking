from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ParkingSpot
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'slots/home.html')

def front(request):
    return render(request, 'slots/front.html')



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




@login_required
def security_view(request):
    if request.method == 'POST':
        spot_number = request.POST.get('spot_number')
        new_status = request.POST.get('status')
        
        try:
            spot = ParkingSpot.objects.get(number=spot_number)
            spot.status = new_status
            spot.save()
            messages.success(request, f'Spot {spot_number} status updated successfully!')
        except ParkingSpot.DoesNotExist:
            messages.error(request, f'Spot {spot_number} not found!')
            
    parking_spots = ParkingSpot.objects.all().order_by('number')
    return render(request, 'registration/security.html', {'parking_spots': parking_spots})

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




