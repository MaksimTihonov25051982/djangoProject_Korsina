from django import forms
from  django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

               ######## Форма для регистрации ########
               # Валидация
def f2(value):
    if not value.isalpha():
        raise forms.ValidationError('Из букв')
    if not value[0].istitle():
        raise forms.ValidationError('Первая буква заглавная.')


class formaRegistr(UserCreationForm):
    username = forms.CharField(label='Логин', help_text='', validators=[f2],
                                widget=forms.TextInput(attrs={'placeholder': 'Abcd'}))
    password1 = forms.CharField(label='Пароль',
                                help_text='',widget=forms.PasswordInput
                                (attrs={'avtocomplete':'new-password'}))
    password2 = forms.CharField(label='Подтверждение',
                                help_text='',widget=forms.PasswordInput
                                (attrs={'avtocomplete': 'new-password'}))
    email = forms.EmailField(label='Почта',
                             widget=forms.TextInput(
                             attrs={'placeholder':'qwe@mail.ru'}))
    first_name = forms.CharField(label='Имя.', required=False, validators=[f2],
                                 widget=forms.TextInput(attrs={'placeholder': 'Иван'}))
    last_name = forms.CharField(label='Фамилия.', required=False, validators=[f2],
                                  widget=forms.TextInput(attrs={'placeholder': 'Иванов'}))

               #######################################




class FormOrder(forms.Form):
    adres = forms.CharField(label='Адрес доставки')
    telefon = forms.CharField(label='Телефон',
                          validators=[RegexValidator('^[+7][0-9]{10}$',
                          message='Неверный формат')],
                          widget=forms.TextInput(attrs={'placeholder': '+70123456789'}))
    nerobot = forms.BooleanField(label='не робот')
