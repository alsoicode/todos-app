from django.shortcuts import render

from todos.models import Todo


def todos_index(request):
    todos = Todo.objects.all()
    return render(request, 'app.html', {'todos': todos})
