from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class PricesTemplateView(TemplateView):
    template_name = 'prices/prices.html'