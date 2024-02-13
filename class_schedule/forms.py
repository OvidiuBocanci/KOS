from django import forms
from django.forms import DateInput, TimeInput, Select, NumberInput

from class_schedule.models import ClassGym



class ClassGymForm(forms.ModelForm):
    class Meta:
        model = ClassGym
        fields = ['title', 'time', 'date', 'people_nr']


        widgets = {
            'title': Select(
                attrs={'class': 'form-select'}),
            'time': TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'people_nr': NumberInput(attrs={'class': 'form-control'}),

        }




class ClassGymUpdateForm(forms.ModelForm):
    class Meta:
        model = ClassGym
        fields = ['title', 'time', 'date', 'people_nr']

        widgets = {
            'title': Select(
                attrs={'class': 'form-select'}),
            'time': TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date', 'format': '%d %m %Y'}),
            'people_nr': NumberInput(attrs={'class': 'form-control'}),

        }
