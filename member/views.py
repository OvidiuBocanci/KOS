from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from member.forms import MemberForm
from member.models import Member


# Create your views here.

class MemberCreateView(CreateView):
    template_name = "member/create_member.html"
    model = Member
    # fields = '__all__'
    form_class = MemberForm
    success_url = reverse_lazy('homepage_gym')

