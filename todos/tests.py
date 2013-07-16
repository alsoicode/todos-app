from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class TodoTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.todos_index_url = reverse('todos_index')

    def test_login_required(self):
        view_names = ['todos_index', 'add_todo', 'complete_todo',
            'clear_completed']

        views = [{'name': view, 'url': reverse(view)}
            for view in view_names]

        for view in views:
            response = self.client.get(view['url'])
            self.assertEqual(response.status_code, 302,
                '{} should not allow unauthenticated requests.'.format(
                    view['name']))
