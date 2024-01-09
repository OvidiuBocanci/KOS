from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class AboutGymTemplateView(TemplateView):
    template_name = 'about_gym/about_gym.html'