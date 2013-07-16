from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from todos.forms import TodoForm
from todos.models import Todo


class TodoFormUnitTestCase(TestCase):
    fixtures = ['users.json']

    def test_set_user_on_todo_form(self):
        user = User.objects.get(username='someone@foo.com')
        form = TodoForm(user=user)
        self.assertIsNotNone(form.user, 'TodoForm.user should '
            'not be None. Instead should be: {}'.format(user))


class TodoTestCase(TestCase):
    fixtures = ['users.json', 'todos.json']

    def setUp(self):
        self.client = Client()

    def log_in_user(self):
        self.client.login(username='someone@foo.com', password='changeme')

    def test_login_required_views(self):
        view_names = ['todos_index', 'add_todo', 'complete_todo',
            'clear_completed']

        views = [{'name': view, 'url': reverse(view)}
            for view in view_names]

        for view in views:
            response = self.client.get(view['url'])
            self.assertEqual(response.status_code, 302,
                '{} should not allow unauthenticated requests.'.format(
                    view['name']))

    def test_todos_index_renders(self):
        self.log_in_user()
        response = self.client.get(reverse('todos_index'))
        self.assertEqual(response.status_code, 200,
            'Todos Index view did not return HTTP 200. '
            'Instead was: {}'.format(response.status_code))

    def test_add_todo(self):
        self.log_in_user()
        data = {'title': 'Another to do'}
        response = self.client.post(reverse('add_todo'),
            data=data)
        self.assertEqual(response.status_code, 200,
            'Add todo view did not return HTTP 200. '
            'Instead was {}'.format(response.status_code))

        todo = Todo.objects.get(title=data['title'])
        self.assertIsNotNone(todo, 'Todo "{}" not created'.format(
            data['title']))

    def test_complete_todo(self):
        self.log_in_user()
        data = {'id': 4}
        response = self.client.post(reverse('complete_todo'),
            data=data)
        self.assertEqual(response.status_code, 200,
            'Complete todo view did not return HTTP 200. '
            'Instead was: {}'.format(response.status_code))

        todo1 = Todo.objects.get(pk=data['id'])
        self.assertIsNotNone(todo1.completed_on, 'Todo id: {0} '
            'from fixtures data initially has no completed_on '
            'date. Posting to the "complete_todo" view should '
            'have added the value of datetime.now()'.format(
                todo1.id))

        # post the same id again to toggle the completed_on
        # datetime back to null
        self.client.post(reverse('complete_todo'),
            data=data)
        todo2 = Todo.objects.get(pk=data['id'])
        self.assertIsNone(todo2.completed_on, 'Todo id: {0} '
            'should not have a completed_on date.'.format(
                todo2.id))

    def test_clear_completed(self):
        self.log_in_user()

        # set todos for user someone@foo.com as completed
        todos = Todo.objects.filter(user__username='someone@foo.com',
            completed_on__isnull=True)

        # these todos are not completed in the fixture data, so set
        # them to completed using the complete_todo view
        url = reverse('complete_todo')
        for todo in todos:
            self.client.post(url, data={'id': todo.id})

        self.client.post(reverse('clear_completed'))

        todo_count = Todo.objects.filter(
            user__username='someone@foo.com').count()
        self.assertEqual(todo_count, 0, 'There should be no todos '
            'remaining for "someone@foo.com". Instead there are: '
            '{}'.format(todo_count))
