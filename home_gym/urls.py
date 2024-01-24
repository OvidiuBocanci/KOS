from django.urls import path

from home_gym import views

urlpatterns = [
    path('homepagegym/', views.HomeGymTemplateView.as_view(), name = 'homepage_gym'),
]