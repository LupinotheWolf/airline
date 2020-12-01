from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flight/index.html", {
        "flight": flight
    })
