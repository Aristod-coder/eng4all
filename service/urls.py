from django.urls import path
from . import views


app_name = 'service'
urlpatterns = [
    path('', views.services, name='services'),
 
    ]
