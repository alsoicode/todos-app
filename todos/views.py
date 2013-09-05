from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from lib.http import JsonResponse
from lib.utils import jsonify
from todos.forms import TodoForm
from todos.models import Todo


@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user)
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
    return JsonResponse(jsonify(response))


@login_required
def complete_todo(request):
    todo = Todo.objects.get(pk=request.POST.get('id'), user=request.user)
    if todo.completed_on:
        todo.completed_on = None
        completed = False
    else:
        todo.completed_on = datetime.now()
        completed = True
    todo.save()
    return JsonResponse(jsonify({'completed': completed}))


@login_required
def clear_completed(request):
    completed_todos = Todo.completed.filter(user=request.user)
    response = {'ids': [c.pk for c in completed_todos]}
    completed_todos.delete()
    return JsonResponse(jsonify(response))
