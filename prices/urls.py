from django.urls import path

from prices import views

urlpatterns = [
    path("prices", views.PricesTemplateView.as_view(), name = "prices")
]