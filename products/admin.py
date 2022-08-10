from django.contrib import admin

from .models import Products, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Products,ProductAdmin)
admin.site.register(Offer)
