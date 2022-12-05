from django.forms import ModelForm
from main.models import *
from betterforms.multiform import MultiModelForm


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ["species", "size", "sex", "age", "lost"]


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ["city", "coordinates", "description"]


class AddAnimalForm(MultiModelForm):
    form_classes = {
        "animal": AnimalForm,
        "advert": AdvertForm
    }
