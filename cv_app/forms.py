# forms.py
from django import forms
from .models import GetContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = GetContactMessage
        fields = ['name', 'email', 'subject', 'message']
