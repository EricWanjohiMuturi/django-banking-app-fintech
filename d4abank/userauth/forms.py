from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User

class UserRegistrationForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'password1' : forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'password2' : forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }