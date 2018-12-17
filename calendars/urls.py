from django.urls import path
from . import views

urlpatterns = [
    path('calendars/',views.calendars,name='calendars'),
]