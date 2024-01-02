from django.shortcuts import render
from .models import Event

def home(request):
    return render(request, "home.html", {})

def event_list(request):
    events = Event.objects.all()
    return render(request, "events.html", {'events':events})