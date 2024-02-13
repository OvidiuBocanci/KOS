from django.shortcuts import render, redirect
import datetime

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from class_schedule.forms import ClassGymForm, ClassGymUpdateForm
from class_schedule.models import ClassGym
from userextend.models import UserSchedule, UserSubscription


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

    def post(self, request, *args, **kwargs):
        class_id = request.POST.get('class_id')

        if request.POST.get('action') == 'join':
            current_user = request.user
            UserSchedule.objects.create(user=current_user,
                                        joined_classes=ClassGym.objects.get(pk=class_id))
            class_instance = ClassGym.objects.get(pk=class_id)
            class_instance.people_nr -= 1
            class_instance.save()


        elif request.POST.get('action') == 'cancel':
            #sterg instanta din userschedule
            UserSchedule.objects.filter(joined_classes_id__id=class_id).delete()

            #modific people_nr din classgym
            class_instance = ClassGym.objects.get(pk=class_id)
            class_instance.people_nr += 1
            class_instance.save()
        return redirect('classes')

    def get_queryset(self):
        return UserSubscription.objects.filter(user_id=self.request.user.id).order_by('-end_date')[:2]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
###########################Start_date - End_date a ultimelor 2 abonamente###########
        last_subscriptions = self.get_queryset()

        if len(last_subscriptions) == 2:
            if last_subscriptions[1].end_date >= datetime.date.today():
                current_subscription = last_subscriptions[1]
                next_subscription = last_subscriptions[0]

            else:
                current_subscription = last_subscriptions[0]
                next_subscription = None

        elif len(last_subscriptions) == 1:
            current_subscription = last_subscriptions[0]
            next_subscription = None

        else:
            current_subscription = None
            next_subscription = None

        context['current_subscription'] = current_subscription
        context['next_subscription'] = next_subscription


        ########################### tuple cu data si clase ###########
        dates = ClassGym.objects.values_list('date', flat=True).distinct().order_by('date')
        current_date = datetime.date.today()

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

        #classes in userschedule
        user_schedule = UserSchedule.objects.values_list('joined_classes_id',  flat=True).filter(user_id=self.request.user.id)
        context['user_schedule'] = user_schedule

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
        current_date = datetime.date.today()

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