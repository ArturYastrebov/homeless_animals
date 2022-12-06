from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, EmailField, CharField
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
User = get_user_model()
class UserCreationForm(UserCreationForm):
    email = EmailField(label="Email")
    phone_number = CharField(label="Phone number")

    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.phone_number = self.cleaned_data["phone_number"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

