from django.shortcuts import render
from django.http import HttpResponse

from main.forms import AnimalForm, AddAnimalForm
from main.models import Animal, Advert, CustomUser


# Create your views here.


def start(response):
    return render(response, "homeless_animals/start.html")


def show_animals_page(response):
    animals = Animal.objects.all()
    adverts = Advert.objects.all()
    return render(
        response,
        "homeless_animals/show_animals.html",
        {"animals": animals, "adverts": adverts},
    )


def about_us_page(response):
    return render(response, "homeless_animals/about_us.html")


def add_animals_page(request):
    form = AddAnimalForm()
    return render(request, "homeless_animals/add_animals.html", {"form": form})


def add_animals_upload(request):
    body = request.body.decode().split("&")[1:]
    values = [i.split("=")[1] for i in body]
    admin = CustomUser.objects.filter(id=1).first()
    animal = Animal.objects.create(
        species=values[0], size=values[1], sex=values[2], age=values[3], lost=values[4]
    )
    advert = Advert.objects.create(
        animal=animal,
        city=values[5],
        coordinates=values[6],
        description=values[7],
        inspector=admin,
    )
    return render(request, "homeless_animals/upload.html")
