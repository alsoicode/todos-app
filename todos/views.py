import json

from django.http import HttpResponse
from django.shortcuts import render

from todos.forms import TodoForm
from todos.models import Todo


def index(request):
    todos = Todo.objects.all()
    form = TodoForm(user=request.user)
    return render(request, 'app.html', {'todos': todos, 'form': form})


def add_todo(request):
    form = TodoForm(request.POST, user=request.user)
    if form.is_valid():
        todo = form.save()
        response = {'id': todo.id, 'title': todo.title}
    else:
        response = form.errors_as_json()
    return HttpResponse(json.dumps(response, ensure_ascii=False))
