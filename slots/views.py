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
