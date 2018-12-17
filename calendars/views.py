from django.shortcuts import render

# Create your views here.
def calendars(request):
    return render(request,'calendars/calendar.html')