import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView

from prices.models import Card
from userextend.forms import UserForm, UserSubscriptionForm, UserPhotoForm
from userextend.models import UserSchedule, UserSubscription, UserPhoto


# Create your views here.

class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

class UserScheduleView(LoginRequiredMixin, ListView,  FormView):
    template_name = 'userextend/profile.html'
    model = UserPhoto
    form_class = UserPhotoForm
    success_url = reverse_lazy('profile')



    def get_queryset(self):
        last_two_subscriptions = UserSubscription.objects.filter(user_id=self.request.user.id).order_by('-end_date')[:2]
        last_photo = UserPhoto.objects.filter(user_id=self.request.user.id).order_by('-created_at').first()
        return last_two_subscriptions, last_photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_subscriptions = self.get_queryset()[0]

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

        #sortez toate clasele dupa user si Date mai mare ca data curenta - le voi afisa in profile
        user_classes = []
        all_user_classes = UserSchedule.objects.filter(user=self.request.user).order_by('joined_classes__date')
        for user_class in all_user_classes:
            if user_class.joined_classes.date >= datetime.date.today():
                user_classes.append(user_class)

        context['user_classes'] = user_classes

        last_photo = self.get_queryset()[1]
        context['last_photo'] = last_photo
        context['show_form'] = self.request.method == 'POST' or not last_photo
        #afisare form UserPhotoForm
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_subscription = form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return redirect('profile')

class UserSubscriptionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'userextend/create_user_subscription.html'
    model = UserSubscription
    form_class = UserSubscriptionForm

    def get_queryset(self):
        return UserSubscription.objects.filter(user_id=self.request.user.id).order_by('-end_date')[:2]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card_id = self.kwargs['card_id']
        card = Card.objects.get(pk=card_id)
        context['card_title'] = card.title
        context['card_price'] = card.price
        context['card_period'] = card.period

        ###########################Start_date - End_date a ultimelor 2 abonamente###########
        last_subscriptions = self.get_queryset()

        if len(last_subscriptions) == 2:
            if last_subscriptions[1].end_date >= datetime.date.today():
                two_active_subscriptions = True
            else:
                two_active_subscriptions = False

        elif len(last_subscriptions) == 1:
            two_active_subscriptions = False

        else:
            two_active_subscriptions = False

        context['two_active_subscriptions'] = two_active_subscriptions


        return context
    def form_valid(self, form):
        if form.is_valid():
            new_subscription = form.save(commit=False)
            new_subscription.user = self.request.user


            card_id = self.kwargs['card_id']
            card = Card.objects.get(pk=card_id)
            new_subscription.subscription = card

            new_subscription.end_date = new_subscription.start_date + datetime.timedelta(days=card.period-1)

            new_subscription.save()
        return redirect('profile')

