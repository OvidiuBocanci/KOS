from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, ListView

from class_schedule.models import ClassGym
from userextend.forms import UserForm
from userextend.models import UserSchedule


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

class UserScheduleView(LoginRequiredMixin, ListView):
    template_name = 'userextend/profile.html'
    model = UserSchedule
    context_object_name = "all_userschedule"
    def post(self, request, *args, **kwargs):

        current_user = request.user
        # class_id = request.POST.get('class_id')
        # class_instance = ClassGym.objects.get(pk=class_id)
        # Creare și salvare instanță a obiectului UserClass
        UserSchedule.objects.create(user=current_user,
                                 joined_classes=ClassGym.objects.get(pk=request.POST.get('class_id')))


        return redirect('classes')

# class UserScheduleView(ListView):
#     template_name = 'class/classes.html'
#     model = ClassGym
#     context_object_name = "all_classes"