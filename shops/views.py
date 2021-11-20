# Django
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView

# Project
from shops.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
