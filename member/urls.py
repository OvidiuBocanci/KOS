from django.urls import path

from member import views

urlpatterns =[
    path("create_member/", views.MemberCreateView.as_view(), name='create-member')
]