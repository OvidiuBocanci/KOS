from django import forms
from django.forms import TextInput

from prices.models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

        widgets = {
            'title': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the title'}),
            'title_detail': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the title_detail'}),
            'price': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the price'}),
            'price_detail': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the price_detail'}),
            'benefit_1': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_1'}),
            'benefit_2': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_2'}),
            'benefit_3': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_3'}),
            'benefit_4': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_4'}),
            'benefit_5': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_5'}),
            'benefit_6': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_6'}),

        }


class CardUpdateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

        widgets = {
            'title': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the title'}),
            'title_detail': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the title_detail'}),
            'price': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the price'}),
            'price_detail': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the price_detail'}),
            'benefit_1': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_1'}),
            'benefit_2': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_2'}),
            'benefit_3': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_3'}),
            'benefit_4': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_4'}),
            'benefit_5': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_5'}),
            'benefit_6': TextInput(
                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Please enter the benefit_6'}),
        }
