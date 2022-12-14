from django import forms
from django import forms
from main.models import *


class FindAnimalAdvertForm(forms.Form):
    SPECIES_CHOICES = [
        ("DOG", "Dog"),
        ("CAT", "Cat"),
    ]
    SIZE_CHOICES = [
        ("L", "Big"),
        ("M", "Middle"),
        ("S", "Small"),
        ("---", "---"),
    ]
    SEX_CHOICES = [("Male", "Male"), ("Female", "Female"), ("---", "---")]
    AGE_CHOICES = [
        ("JN", "Junior"),
        ("MD", "Middle"),
        ("SN", "Senior"),
        ("---", "---"),
    ]
    LOST_CHOICES = [("YES", "Yes"), ("No", "No"), ("---", "---")]
    CITY_CHOICES = [
        ("KV", "Kyiv"),
    ]

    species = forms.ChoiceField(choices=SPECIES_CHOICES)
    size = forms.ChoiceField(choices=SIZE_CHOICES)
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    age = forms.ChoiceField(choices=AGE_CHOICES)
    lost = forms.ChoiceField(choices=LOST_CHOICES)
    city = forms.ChoiceField(choices=CITY_CHOICES)


class AddAnimalAdvertForm(forms.ModelForm):
    class Meta:
        model = AnimalAdvert
        fields = [
            "city",
            "coordinates",
            "description",
            "photo",
            "species",
            "size",
            "sex",
            "age",
            "lost",
        ]
