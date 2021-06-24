# from django.shortcuts import render, redirect
#
# from todos_app.todos.forms import CreateTodoForm
# from todos_app.todos.models import Todo
# from todos_app.todos.models.todo import Person
#
#
# def index(req):
#     context = {
#         'todos': Todo.objects.all(),
#         'form': CreateTodoForm(),
#     }
#
#     return render(req, 'index.html', context)
#
#
# # def create_todo(req):
# #     text = req.POST['text']
# #     description = req.POST['description']
# #     owner_name = req.POST['owner']
# #     owner = Person.objects\
# #         .filter(name=owner_name)\
# #         .first()
# #
# #     if not owner:
# #         owner = Person(name=owner_name)
# #         owner.save()
# #
# #     todo = Todo(
# #         text=text,
# #         description=description,
# #         owner=owner,
# #     )
# #     todo.save()
# #
# #     return redirect('')
#
#
# def create_todo(req):
#     form = CreateTodoForm(req.POST)
#
#     if form.is_valid():
#         text = form.cleaned_data['text']
#         description = form.cleaned_data['description']
#         todo = Todo(
#             text=text,
#             description=description,
#             # owner=owner,
#         )
#         todo.save()
#         return redirect('/')
#     else:
#         context = {
#             'todos': Todo.objects.all(),
#             'form': form,
#         }
#
#         return render(req, 'index.html', context)
#
#
# def change_todo_state(req, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#     return redirect('/')
from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm, TodoForm
from todos_app.todos.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'todo_app/index.html', context)


def create_todo2(request):
    form = TodoForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'todo_app/create.html', context)


# def create_todo(request):
#     form = CreateTodoForm(request.POST)
#
#     if request.method == "POST":
#         if form.is_valid():
#             todo = Todo(
#                 title=form.cleaned_data['title'],
#                 description=form.cleaned_data['description'],
#                 state=False,
#             )
#             todo.save()
#             return redirect('index')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'todo_app/create.html', context)


def show_form(request, form):
    context = {
        'form': form,
    }
    return render(request, 'todo_app/edit.html', context)


def update_todo2(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == "GET":
        return show_form(request, TodoForm(initial=todo.__dict__))

    else:
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            todo.save()
            return redirect('index')

        return show_form(request, form)

# def update_todo(request, pk):
#     todo = Todo.objects.get(pk=pk)
#
#     if request.method == "GET":
#         context = {
#             'form': UpdateTodoForm(initial=todo.__dict__)
#         }
#         return render(request, 'todo_app/edit.html', context)
#
#     else:
#         form = UpdateTodoForm(request.POST)
#
#         if form.is_valid():
#             todo.title = form.cleaned_data['title']
#             todo.description = form.cleaned_data['description']
#             todo.state = form.cleaned_data['state']
#
#             todo.save()
#             return redirect('index')


def delete_todo(request, pk):
    if request.method == "GET":
        context = {
            "form": "Are you sure you want to delete this Todo?",
        }
        return render(request, 'todo_app/delete.html', context)
    else:
        todo = Todo.objects.get(pk=pk)

        todo.delete()
        return redirect('index')