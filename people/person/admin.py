from django.contrib import admin

from .models import Person, Address


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "address")
    list_editable = ("first_name", "last_name", "address")


admin.site.register(Address)