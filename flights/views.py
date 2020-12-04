from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "flights": Flight.objects.all(),
        })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flight=flight).all(),
        "meal": flight.meal.all(),
    })

#Only activates if a POST request is made
def book(request, flight_id):
    if request.method == "POST":
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        flight = Flight.objects.get(pk=flight_id)
        passenger.flight.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

def food(request):
    food = Food.objects.all()
    return render(request, "food.html", {
        "food": food,
    })
