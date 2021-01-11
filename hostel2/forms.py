from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm
from .models import AlumniTestimony



class AlumniForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    year = forms.IntegerField()
    branch = forms.CharField()
    testimony = forms.CharField()
    pic = forms.ImageField()



    class Meta:
        model = AlumniTestimony
        fields = ['name', 'email', 'year', 'branch','testimony','pic' ]
