from django.urls import path

from userextend import views

urlpatterns = [
    path("create_user/", views.UserCreateView.as_view(), name='create-user'),
    path('user_subscription/<int:card_id>/', views.UserSubscriptionCreateView.as_view(), name='user-subscription'),
    path('profile/', views.UserScheduleView.as_view(), name='profile'),

]
