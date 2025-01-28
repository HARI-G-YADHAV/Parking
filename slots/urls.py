from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('home/', views.home, name='home'),
    path('security/', views.security_page, name='security'),
    path('api/parking-spots/', views.parking_spots_api, name='parking-spots-api'),
]