from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('signin',signin,name='signin'),
    path('register',register,name='register'),
    path('patientregistration',patientregistration,name='patientregistration'),
    
]