from django.shortcuts import render
from django.http import HttpResponse

from main.forms import AnimalForm


# from main.forms import AnimalForm, AddAnimalForm


# Create your views here.


def start(response):
    return render(response, "homeless_animals/start.html")


def show_animals_page(response):
    return render(response, "homeless_animals/show_animals.html")


def about_us_page(response):
    return render(response, "homeless_animals/about_us.html")


def add_animals_page(request):
    form = AnimalForm()
    return render(request, 'homeless_animals/add_animals.html', {'form': form})
