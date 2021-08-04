from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'category', 'title', 'price', 'date')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date_reservation')
    list_display_links = ('id', 'name', 'date_reservation')
    search_fields = ('id', 'name', 'date_reservation', 'email')


class ChefAdmin(admin.ModelAdmin):
    list_display = ('id', 'chef_name')
    list_display_links = ('id', 'chef_name')
    search_fields = ('id', 'chef_name', 'chef_last_name', 'chef_profession')


admin.site.register(Chefs, ChefAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)