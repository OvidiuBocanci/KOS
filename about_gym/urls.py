from django.urls import path

from about_gym import views

urlpatterns = [
    path('about-gym', views.AboutGymTemplateView.as_view(), name = 'about_gym')
]