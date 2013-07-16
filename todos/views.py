from datetime import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from todos.forms import TodoForm
from todos.models import Todo


@login_required
def index(request):
    todos = Todo.objects.all()
    form = TodoForm(user=request.user)
    return render(request, 'app.html', {'todos': todos, 'form': form})


@login_required
def add_todo(request):
    form = TodoForm(request.POST, user=request.user)
    if form.is_valid():
        todo = form.save()
        response = {'id': todo.id, 'title': todo.title}
    else:
        response = form.errors_as_json()
    return HttpResponse(json.dumps(response, ensure_ascii=False))


@login_required
def complete_todo(request):
    todo = Todo.objects.get(pk=request.POST.get('id'))
    if todo.completed_on:
        todo.completed_on = None
        completed = False
    else:
        todo.completed_on = datetime.now()
        completed = True
    todo.save()
    response = {'completed': completed}
    return HttpResponse(json.dumps(response, ensure_ascii=False))


@login_required
def clear_completed(request):
    completed_todos = Todo.objects.filter(completed_on__isnull=False)
    response = {'ids': [c.pk for c in completed_todos]}
    completed_todos.delete()
    return HttpResponse(json.dumps(response, ensure_ascii=False))
