from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home_page, name='home'),
    path('login/', views.user_login, name='login'),
    path('registration/security', views.security_page, name='security'),
    path('api/parking-spots/', views.get_parking_spots, name='parking-spots'),
=======
    path('', views.front, name='front'),
    path('home/', views.home, name='home'),
    path('security/', views.security_page, name='security'),
    path('api/parking-spots/', views.parking_spots_api, name='parking-spots-api'),
>>>>>>> f7706be1b236887ea082825bd5300320dea22d29
]