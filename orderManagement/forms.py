from django import forms
from django.contrib.auth.models import User
from .models import Profile


class userLogin(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': ' USERNAME'}) )
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder': ' PASSWORD'}))


class userSignup(forms.ModelForm):
    password = forms.CharField(max_length=50, widget = forms.PasswordInput())
    password2 = forms.CharField(max_length=50, widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password', 'password2',  'email')


class userSignup_profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone',)