from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path("login/", login_request, name="login"),
    # path('signin',signin,name='signin'),
    path('registration',registration,name='registration'),
    path('inner',inner,name="inner"),
    
]