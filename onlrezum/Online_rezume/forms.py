from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    

    username = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Введите ваш Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput
                            (attrs={'placeholder':'Введите пароль', 'font-weight':'bold'}))
    password2 = forms.CharField(widget=forms.PasswordInput
                            (attrs={'placeholder':'Повторите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    

class LoginUserForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Введите ваш Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput
                            (attrs={'placeholder':'Введите пароль', 'font-weight':'bold'}))

    class Meta:
        model = User
        fields = ['username', 'password1']