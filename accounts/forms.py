from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class CreateAccountForm(UserCreationForm):
    username = forms.EmailField(max_length=75, label='Email')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=75, label='Email')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = 'Password'
