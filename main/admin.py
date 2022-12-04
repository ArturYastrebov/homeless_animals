from django.contrib import admin
from .models import User, Animal, Advert


class UserAdmin(admin.ModelAdmin):
    list_display = ("nick_name", "email", "name", "phone_number", "password", "permission")

class AnimalAdmin(admin.ModelAdmin):
    list_display = ("species", "size", "sex", "age", "lost")

class AdvertAdmin(admin.ModelAdmin):
    list_display = ("created", "last_updated", "status", "animal_id", "sity", "coordinates", "description", "inspector_id")

admin.site.register(User, UserAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Advert, AdvertAdmin)

