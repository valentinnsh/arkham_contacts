from django.contrib import admin
from .models import Expansions, Locations, Contacts

# Register your models here.


class ExpansionsAdmin(admin.ModelAdmin):
    list_display = ('expansion_name', 'display_creator')

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'district')

class ContactsAdmin(admin.ModelAdmin):
    pass



admin.site.register(Expansions, ExpansionsAdmin)
admin.site.register(Locations, LocationsAdmin)
admin.site.register(Contacts, ContactsAdmin)
