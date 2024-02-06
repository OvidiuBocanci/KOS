from django.urls import path

from class_schedule import views

urlpatterns = [
    path("classes/", views.ClassListView.as_view(), name="classes"),
    path("create_class/", views.ClassCreateView.as_view(), name="create-class"),
    path("update_class/<int:pk>/", views.ClassUpdateView.as_view(), name="update-class"),
    path("delete_class/<int:pk>/", views.ClassDeleteView.as_view(), name="delete-class"),
    path("my_classes/", views.MyClassListView.as_view(), name="my-classes"),
]