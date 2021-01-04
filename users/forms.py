from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

COLOR_CHOICES = (
    ('Green','GREEN'),
    ('Blue', 'BLUE'),
    ('Red','RED'),
    ('Orange','ORANGE'),
    ('Black','BLACK'),
)


class ProfileUpdateForm(forms.ModelForm):
    interests = forms.MultipleChoiceField(choices=COLOR_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Profile
        fields = ['image', 'roll_no', 'room_no', 'interests']

