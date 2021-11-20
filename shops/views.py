# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Project
from shops.models import Invoice


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice_details.html'
