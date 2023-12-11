from django import forms
from .models import *


class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['eventname', 'description', 'date', 'enrollurl']
        widgets = {
            'eventname': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'enrollurl': forms.URLInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['enrollurl'].required = False


class BudgetAssignForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['assigned_budget']
        widgets = {
            'assigned_budget': forms.NumberInput(attrs={'class':'form-control'})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['assigned_budget'].required = False


class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'event', 'start_date', 'end_date']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class ClubInfoForm(forms.ModelForm):
    class Meta:
        model = ClubInfo
        exclude = ['club'] 
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'contact_mail': forms.EmailInput(attrs={'class': 'form-control'}),  
            'photo': forms.ClearableFileInput(attrs={'class': 'custom-file-input form-control'}),  
        }
