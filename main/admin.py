from django.contrib import admin
from .models import CustomUser, Animal, Advert


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "phone_number", "password", "is_staff")

class AnimalAdmin(admin.ModelAdmin):
    list_display = ("species", "size", "sex", "age", "lost")

class AdvertAdmin(admin.ModelAdmin):
    list_display = ("created", "last_updated", "status", "animal_id", "city", "coordinates", "description", "inspector_id")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Advert, AdvertAdmin)

