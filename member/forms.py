from django import forms
from django.forms import TextInput, DateInput, NumberInput, EmailInput, Select

from member.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
       model = Member
       fields = '__all__'

       widgets = {
           'first_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your first name'}),
           'last_name': TextInput(attrs={'class':'form-control', 'placeholder':'Please enter your last name'}),
           'birth_date': DateInput(attrs={'class':'form-control', 'type':'date'}),
           'phone_number': NumberInput(attrs={'class':'form-control', 'placeholder':'Please enter your phone number'}),
           'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
           'gender': Select(attrs={'class': 'form-select'}),
           'profile': forms.ClearableFileInput(attrs={'class':'form-control'}),
       }


    