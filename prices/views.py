import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from prices.forms import CardForm, CardUpdateForm
from prices.models import Card
from userextend.models import UserSubscription


# Create your views here.

class PricesTemplateView(TemplateView):
    template_name = 'prices/prices.html'


class CardCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'prices/create_card.html'
    model = Card
    form_class = CardForm
    success_url = reverse_lazy('prices')
    permission_required = 'prices.add_card'

    def form_valid(self, form):
        if form.is_valid():
            new_card = form.save(commit=False)

            if new_card.period <= 30:
                new_card.display_price = new_card.price
            else:
                months = new_card.period // 30
                new_card.display_price = new_card.price // months
            new_card.save()
        return redirect('prices')

class CardListView(ListView):
    template_name = 'prices/prices.html'
    model = Card
    context_object_name = "all_cards"


class CardUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    template_name = 'prices/update_card.html'
    model = Card
    form_class = CardUpdateForm
    success_url = reverse_lazy('prices')
    permission_required = 'prices.change_card'
    def form_valid(self, form):
        if form.is_valid():
            new_card = form.save(commit=False)

            if new_card.period <= 30:
                new_card.display_price = new_card.price
            else:
                months = new_card.period // 30
                new_card.display_price = new_card.price // months
            new_card.save()
        return redirect('prices')

class CardDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    template_name = 'prices/delete_card.html'
    model = Card
    success_url = reverse_lazy('prices')
    permission_required = 'prices.delete_card'

