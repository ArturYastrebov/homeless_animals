from django.contrib import admin
from .models import CustomUser, AnimalAdvert


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "phone_number", "password", "is_staff")


class AnimalAdvertAdmin(admin.ModelAdmin):
    list_display = ("created", "last_updated", "status", "city", "coordinates", "description", "inspector_id", "species", "size", "sex", "age", "lost")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AnimalAdvert, AnimalAdvertAdmin)

