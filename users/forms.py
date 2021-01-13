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


SPORTS_CHOICES = (
    ('Cricket','CRICKET'),
    ('Hockey', 'HOCKEY'),
    ('Football','FOOTBALL'),
    ('Swimming','SWIMMING'),
    ('Badminton','BADMINTON'),
    ('Athletics','ATHLETICS'),
    ('Weight Lifting','WEIGHT LIFTING'),
    ('Tennis','TENNIS'),
    ('Basketball','BASKETBALL'),
)

CULT_CHOICES = (
    ('Dance','DANCE'),
    ('Singing', 'SINGING'),
    ('Instruments','INSTRUMENTS'),
    ('Dramatics','DRAMATICS'),
    ('Fashion','FASHION'),
)

TECH_CHOICES = (
    ('CP','CP'),
    ('Robotics', 'ROBOTICS'),
    ('Classical Maths & Physics','CLASSICAL MATHS & PHYSICS'),
)


class ProfileUpdateForm(forms.ModelForm):
    interests_sports = forms.MultipleChoiceField(choices=SPORTS_CHOICES, widget=forms.CheckboxSelectMultiple,required=False)
    interests_cult = forms.MultipleChoiceField(choices=CULT_CHOICES, widget=forms.CheckboxSelectMultiple,required=False)
    interests_tech = forms.MultipleChoiceField(choices=TECH_CHOICES, widget=forms.CheckboxSelectMultiple,required=False)
    class Meta:
        model = Profile
        fields = ['image', 'roll_no', 'room_no', 'interests_sports', 'interests_cult', 'interests_tech','year','department']