from django.contrib import admin

from shops.models import Address, Order, Status


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['status']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
