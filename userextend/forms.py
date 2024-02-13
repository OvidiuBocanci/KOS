import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import DateInput, NumberInput, TextInput

from userextend.models import UserSubscription


class AuthenticationNewForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Please enter your username'})
        self.fields['password'].widget.attrs.update({'class':'form-control', 'placeholder':'Please enter your password'})


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  # 'phone_number'
                      )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter your password confirmation'})

class UserSubscriptionForm(forms.ModelForm):

    class Meta:
        model = UserSubscription
        fields = ['start_date', 'card_number', 'terms_and_conditions']

        widgets = {
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'card_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter last 4 digits'}),
        }


    def clean(self):
        cleaned_data = self.cleaned_data

        subscription_date = cleaned_data['start_date']
        if subscription_date < datetime.date.today():
            msg = 'Start date trebuie sa fie egala sau mai mare decat data curenta'
            self._errors['start_date'] = self.error_class([msg])

        card_number = cleaned_data['card_number']
        try:
            int(card_number)
        except:
            msg = 'Nu ati introdus corect cele 4 cifre'
            self._errors['card_number'] = self.error_class([msg])

        terms = cleaned_data['terms_and_conditions']
        if terms != True:
            msg = 'Nu ati acceptat termenii si conditiile'
            self._errors['terms_and_conditions'] = self.error_class([msg])



        return cleaned_data
