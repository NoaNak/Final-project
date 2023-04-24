from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate
from django import forms

# 1. SignInForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = 'User'
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# from django import forms
# from django.contrib.auth.forms import AuthenticationForm

# class ConnexionForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
