from PIL import Image

from django.shortcuts import render
from django.core.paginator import Paginator

from main.forms import AddAnimalAdvertForm, FindAnimalAdvertForm
from main.models import Animal, Advert


# Create your views here.


def start(response):
    return render(response, "homeless_animals/start.html")


def about_us_page(response):
    return render(response, "homeless_animals/about_us.html")


def show_animals_page(request):
    form = FindAnimalAdvertForm()
    return render(request, "homeless_animals/add_animals.html", {"form": form})


class AnimalAdvert:
    def __init__(self, animal: Animal, advert: Advert):
        self.animal = animal
        self.advert = advert


def filter_animals_and_adverts(filters):
    animals = Animal.objects.filter(species=filters["species"])
    adverts = Advert.objects.filter(city=filters["city"])
    if "size" in filters:
        animals = animals.filter(size=filters["size"])
    if "sex" in filters:
        animals = animals.filter(sex=filters["sex"])
    if "age" in filters:
        animals = animals.filter(age=filters["age"])
    if "lost" in filters:
        animals = animals.filter(lost=filters["lost"])
    animal_adverts = []
    for animal in animals:
        try:
            advert = adverts.get(animal_id=animal.id)
            # if advert:
            animal_adverts.append((animal, advert))
        except Exception:
            print("There is no adverts")
    return animal_adverts


def show_animals_upload(request):
    body = request.body.decode().split("&")[1:8]
    filters = {i.split("=")[0]: i.split("=")[1] for i in body if i.split("=")[1] != ""}
    animals_adverts_list = filter_animals_and_adverts(filters)
    animal_advert = []
    for element in animals_adverts_list:
        animal_advert.append(AnimalAdvert(element[0], element[1]))

    paginator = Paginator(animal_advert, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "homeless_animals/show_animals_upload.html", {"page_obj": page_obj}
    )


def add_animals_page(request):
    form = AddAnimalAdvertForm()
    return render(request, "homeless_animals/add_animals.html", {"form": form})


def add_animals_upload(request):
    body = request.body.decode().split("&")[1:]
    values = [i.split("=")[1] for i in body]
    animal = Animal.objects.create(
        species=values[0], size=values[1], sex=values[2], age=values[3], lost=values[4]
    )
    Advert.objects.create(
        animal=animal,
        city=values[5],
        coordinates=values[6],
        description=values[7],
        photo=values[8],
    )
    # path = r"main/static/images/{filename}".format(filename=values[8])
    # img = Image.open(path)
    # img = img.save(f"{values[8]}")
    return render(request, "homeless_animals/upload.html")
