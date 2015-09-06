from django.contrib import admin

from .models import Country, HotSpot

class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display_links = ('id',)
    list_display = ('id', 'name', 'iso2', 'iso3', 'pop2005')


class HotSpotAdmin(admin.ModelAdmin):
    model = HotSpot
    list_display_links = ('id', )
    list_display = ('id', )


admin.site.register(Country, CountryAdmin)
admin.site.register(HotSpot, HotSpotAdmin)
