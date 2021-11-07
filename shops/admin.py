# Django
from django.contrib import admin

# Project
from shops.models import Address
from shops.models import Order
from shops.models import Status


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['status']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
