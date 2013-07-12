# from django import forms

from lib.forms import AjaxModelForm
from todos.models import Todo


class TodoForm(AjaxModelForm):
    class Meta:
        model = Todo

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(TodoForm, self).__init__(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, commit=True):
        instance = super(TodoForm, self).save(commit=False)
        if commit:
            instance.user = self.user
            instance.save()
        return instance
