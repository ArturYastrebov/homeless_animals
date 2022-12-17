from django import forms
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, EmailField, CharField, IntegerField
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

#
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


User = get_user_model()
class UserCreationForm(UserCreationForm):
    email = EmailField(label="Email")
    phone_number = IntegerField(label="Phone number")



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs = {'class': 'form-control', "placeholder": "name@example.com"}
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

