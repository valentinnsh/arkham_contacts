from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expansions, Locations, Contacts

class RandomContactForm(forms.Form):
    locate = forms.ModelChoiceField(queryset = Locations.objects.all())

    expansion = forms.ModelMultipleChoiceField(queryset = Expansions.objects.all())

    
    