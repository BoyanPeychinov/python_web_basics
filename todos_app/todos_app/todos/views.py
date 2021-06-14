from django.shortcuts import render, redirect

from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person


def index(req):
    context = {
        'todos': Todo.objects.all(),
    }

    return render(req, 'index.html', context)


def create_todo(req):
    text = req.POST['text']
    description = req.POST['description']
    owner_name = req.POST['owner']
    owner = Person.objects\
        .filter(name=owner_name)\
        .first()

    if not owner:
        owner = Person(name=owner_name)
        owner.save()

    todo = Todo(
        text=text,
        description=description,
        owner=owner,
    )
    todo.save()

    return redirect('')
