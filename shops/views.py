# Django
from django.shortcuts import render
from django.views.generic import ListView

# Project
from shops.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
