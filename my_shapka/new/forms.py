from django import forms
from .models import *
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password_check = forms.CharField(widget=forms.PasswordInput, label='Повтор пароля')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    class Meta:
        model = User
        fields = ['username', 'password', 'password_check', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Логин',
            'first_name': 'Ваше имя',
            'last_name': 'Ваша фамилия',
            'email': 'Email',
        }
        help_texts = {
            'password': 'придумайте пароль не совсем простой',
            'email': 'указывайте реальный адрес, т.к. на него придёт подтверждение'
        }

    def clean(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с данным логином уже зарегистрирован в системе!', code='user exists',)