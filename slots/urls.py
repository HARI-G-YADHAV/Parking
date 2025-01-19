from django.urls import path
from .views import *

urlpatterns=[
    path('',home_page,name='home_page'),
    path('security/',security_page,name='security_page')
]