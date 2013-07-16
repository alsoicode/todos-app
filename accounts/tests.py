from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from accounts.forms import CreateAccountForm


class CreateAccountFormTestCase(TestCase):
    def setUp(self):
        self.data = {'username': 'test@user.com',
            'password1': 'changeme', 'password2': 'changeme'}

    def test_honeypot(self):
        data = self.data.update({'honeypot': 'some value'})
        form = CreateAccountForm(data=data)
        self.assertFalse(form.is_valid(), 'Honeypot field should not be '
            'valid if it contains a value')

    def test_valid_form(self):
        form = CreateAccountForm(data=self.data)
        self.assertTrue(form.is_valid(), 'CreateAccountForm had the '
            'following errors: {}'.format(form.errors))


class AccountLoginTestCase(TestCase):
    fixtures = ['test-users.json']

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')

    def test_login_get(self):
        response = self.client.get(self.login_url)
        login_form = response.context['form']
        self.assertIsNotNone(login_form, 'Login view did not have login form '
            'present in context.')
        self.assertEqual(response.status_code, 200,
            'Login view did not render.')

    def test_login_post(self):
        data = {'username': 'test@user.com', 'password': 'changeme'}
        response = self.client.post(self.login_url, data=data)
        self.assertEquals(response.status_code, 302, 'Login form did not '
            'sucessfully redirect to todos index view.')


class CreateAccountTestCase(TestCase):
    def test_create_account(self):
        data = {'username': 'another@user.com', 'password1': 'secure',
            'password2': 'secure'}
        response = self.client.post(reverse('create_account'), data=data)
        self.assertEquals(response.status_code, 302, 'Create account view '
            'should have redirected to the todos index view. Instead, status '
            'code was {}'.format(response.status_code))
        self.assertIsNotNone(User.objects.get(username=data['username']))
