from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeGymTemplateView(TemplateView):
    template_name = 'home_gym/homepagegym.html'