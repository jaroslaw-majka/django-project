# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

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


class InvoiceUpdateView(UpdateView):
    model = Invoice
    fields = '__all__'
    template_name = 'invoice_update.html'
    success_url = reverse_lazy('invoice_list')


class InvoiceCreateView(CreateView):
    model = Invoice
    fields = '__all__'
    template_name = 'invoice_create.html'
    success_url = reverse_lazy('invoice_list')
