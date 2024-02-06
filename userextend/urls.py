from django.urls import path

from userextend import views

urlpatterns = [
    path("create_user/", views.UserCreateView.as_view(), name='create-user'),
    path('user_schedule/<int:classgym_id>/', views.UserScheduleView.as_view(), name='user-schedule'),
    path('profile/', views.UserScheduleView.as_view(), name='profile'),
]
