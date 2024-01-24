from django.urls import path

from prices import views

urlpatterns = [
    path("prices/", views.CardListView.as_view(), name = "prices"),
    path("create_card/", views.CardCreateView.as_view(), name = "create-card"),
    path("update_card/<int:pk>/", views.CardUpdateView.as_view(), name = "update-card"),
    path("delete_card/<int:pk>/", views.CardDeleteView.as_view(), name = "delete-card"),


]