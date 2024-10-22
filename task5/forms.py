from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Имя пользователя:')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль:', min_length=8)
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль:', min_length=8)
    age = forms.IntegerField(min_value=18, label='Возраст:', max_value=120)
