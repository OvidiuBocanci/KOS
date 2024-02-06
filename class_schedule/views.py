from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from class_schedule.forms import ClassGymForm, ClassGymUpdateForm
from class_schedule.models import ClassGym


class ClassCreateView(LoginRequiredMixin, CreateView):
    template_name = 'class/create_class.html'
    model = ClassGym
    form_class = ClassGymForm
    success_url = reverse_lazy('classes')
    permission_required = 'class_schedule.add_classgym'

    def form_valid(self, form):
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.trainer = self.request.user
            new_class.save()
        return redirect('my-classes')

class ClassListView(ListView):
    template_name = 'class/classes.html'
    model = ClassGym
    context_object_name = "all_classes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dates = ClassGym.objects.values_list('date', flat=True).distinct().order_by('date')
        current_date = datetime.now().date()

        days = 0
        dates_classes = []
        for date in dates:
            if date >= current_date and days < 7:
                dates_classes.append(date)
                days += 1

        tuple_classes = []
        for el in dates_classes:
            time_classes = ClassGym.objects.filter(date=el).distinct().order_by('time')
            tuple_classes.append((el, time_classes))

        context['tuple_list'] = tuple_classes
        context['crt_date'] = current_date
        return context



class ClassUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    template_name = 'class/update_class.html'
    model = ClassGym
    form_class = ClassGymUpdateForm
    success_url = reverse_lazy('my-classes')
    permission_required = 'class_schedule.change_classgym'

class ClassDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    template_name = 'class/delete_class.html'
    model = ClassGym
    success_url = reverse_lazy('my-classes')
    permission_required = 'class_schedule.delete_classgym'

class MyClassListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    template_name = 'class/my_classes.html'
    model = ClassGym
    context_object_name = "all_myclasses"
    permission_required = 'class_schedule.trainer_schedule'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dates = ClassGym.objects.filter(trainer_id=self.request.user.id).values_list('date', flat=True).distinct().order_by('date')
        current_date = datetime.now().date()

        dates_classes = []
        for date in dates:
            if date >= current_date:
                dates_classes.append(date)

        tuple_classes = []
        for el in dates_classes:
            time_classes = ClassGym.objects.filter(date=el).distinct().order_by('time')
            tuple_classes.append((el, time_classes))


        context['tuple_list'] = tuple_classes
        context['crt_date'] = current_date
        return context