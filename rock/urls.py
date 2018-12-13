from django.urls import path
from . import views

urlpatterns = [
    path('rps/',views.index,name='rps'),
]