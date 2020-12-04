from django.urls import path
from . import views

#<int:flight_id> will take the number in the path and place the flight id in the var
urlpatterns = [
    path("", views.index, name='index'),
    path("<int:flight_id>/", views.flight, name='flight'),
    path("food/", views.food, name='food'),
    path("<int:flight_id>/book/", views.book, name='book'),
]
