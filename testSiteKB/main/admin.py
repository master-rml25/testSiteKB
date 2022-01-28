from django.contrib import admin
from main.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("operator", "organisation")
