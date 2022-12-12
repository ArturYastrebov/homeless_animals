from django.forms import ModelForm, Form
from django import forms
from main.models import *
from betterforms.multiform import MultiModelForm


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


class AddAnimalAdvertForm(forms.Form):
    STATUS_CHOICES = [("IN_PROCESS", "In process"), ("DONE", "Done")]
    SPECIES_CHOICES = [
        ("DOG", "Dog"),
        ("CAT", "Cat"),
    ]
    SIZE_CHOICES = [
        ("L", "Big"),
        ("M", "Middle"),
        ("S", "Small"),
    ]
    SEX_CHOICES = [("Male", "Male"), ("Female", "Female")]
    AGE_CHOICES = [
        ("JN", "Junior"),
        ("MD", "Middle"),
        ("SN", "Senior"),
    ]
    LOST_CHOICES = [("YES", "Yes"), ("No", "No")]
    CITY_CHOICES = [
        ("KV", "Kyiv"),
    ]

    # photo = models.FileField(null=True)
    species = forms.ChoiceField(choices=SPECIES_CHOICES)
    size = forms.ChoiceField(choices=SIZE_CHOICES)
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    age = forms.ChoiceField(choices=AGE_CHOICES)
    lost = forms.ChoiceField(choices=LOST_CHOICES)
    city = forms.ChoiceField(choices=CITY_CHOICES)
    coordinates = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    photo = forms.FileField()
