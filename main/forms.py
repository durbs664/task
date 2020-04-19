from django import forms
from .models import Service_Provider

class ServiceP_Form(forms.ModelForm):
    class Meta:
        model       = Service_Provider

        fields = ('name', 'panno', 'about', 'location', 'contactno', 'averageRating', 'image')
