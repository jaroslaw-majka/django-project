# Django
from django.db import models


class Address(models.Model):
    local_no = models.CharField(
        'nr lokalu',
        max_length=10,
        blank=True
    )
    building = models.CharField(
        'nr budynku',
        max_length=10
    )
    street = models.CharField(
        'ulica',
        max_length=40
    )
    city = models.CharField(
        'miasto',
        max_length=40
    )
    zip_code = models.CharField(
        'kod pocztowy',
        max_length=10
    )


class Warehouse(models.Model):
    name = models.CharField(
        'nazwa',
        max_length=10
    )
    # Improtuje pola z powyższej klasy Address
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        verbose_name='adres'
    )
    capacity = models.IntegerField(
        'ilość produktów',
        blank=True,
        default=0
    )


class Shop(models.Model):
    name = models.CharField(
        'nazwa',
        max_length=10,
        blank=True
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        verbose_name='adres',
        blank=True,
        null=True
    )


class Status(models.Model):
    name = models.CharField(
        'nazwa',
        max_length=50
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.CharField(
        'numer zamówienia',
        max_length=50,
        blank=True
    )
    shipping_address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        verbose_name='adres do wysyłki',
        blank=True,
        null=True,
        related_name='shipping_addreses'
    )
    invoice_address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        verbose_name='adres do faktury',
        related_name='invoice_addresses',
        null=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name='status'
    )
    creation_date = models.DateField(
        'data utworzenia',
        auto_now=True,
        blank=True,
        null=True
    )


class Discount(models.Model):
    pass


class ShippingMethod(models.Model):
    name = models.CharField(
        'nazwa',
        max_length=10,
        blank=True
    )
    price = models.DecimalField(
        'kwota wysyłki',
        decimal_places=2,
        max_digits=5,
        blank=True,
        default=0.00
    )


class PaymentMethod(models.Model):
    pass


class Product(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='zamówienie',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    in_stock = models.IntegerField(
        'stan magazynowy',
        blank=True,
        default=0
    )
