from django.urls import path

from todos_app.todos.views import index, create_todo

urlpatterns = [
    path('', index),
    path('todos-add', create_todo)
]