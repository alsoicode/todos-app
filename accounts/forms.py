from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class CreateAccountForm(UserCreationForm):
    username = forms.EmailField(max_length=75, label='Email')
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_honeypot(self):
        value = self.cleaned_data.get('honeypot')
        if value != '':
            raise forms.ValidationError(u'Automated form submissions'
                'are not allowed')
        return value


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=75, label='Email')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = 'Password'
