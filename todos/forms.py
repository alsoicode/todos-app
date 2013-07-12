from django import forms

from todos.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
