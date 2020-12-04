from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    #passengers is referenced in class Passenger
    #meal is referenced in class Food

    def __str__(self):
        return f" {self.id}: From {self.origin} To {self.destination}"

class Food(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.type} Meal"

class Passenger(models.Model):
    surname = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    food_choice = models.ManyToManyField(Food, blank=True, related_name="food_choice")
    meal = models.ManyToManyField(Flight, blank=True, related_name="meal")

    def __str__(self):
        return f"{self.surname}, {self.first_name}"
