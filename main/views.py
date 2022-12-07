from django.shortcuts import render

from main.forms import AddAnimalForm
from main.models import Animal, Advert, CustomUser


# Create your views here.


def start(response):
    return render(response, "homeless_animals/start.html")


def open_animals_page(response):
    animals = sorted(Animal.objects.all(), key=lambda instance: instance.id)
    adverts = sorted(Advert.objects.all(), key=lambda instance: instance.animal_id)
    results = [str(result[0]) + str(result[1]) for result in list(zip(animals, adverts))]
    return render(
        response,
        "homeless_animals/show_animals.html",
        {"content": results},
    )


def show_proper_animals():
    pass


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
    Advert.objects.create(
        animal=animal,
        photo=values[5],
        city=values[6],
        coordinates=values[7],
        description=values[8],
        inspector=admin,
    )
    return render(request, "homeless_animals/upload.html")
