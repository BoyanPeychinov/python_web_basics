from django.urls import path

from todos_app.todos.views import index, create_todo, update_todo, delete_todo

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_todo, name='create todo'),
    path('update/<int:pk>/', update_todo, name='update todo'),
    path('delete/<int:pk>/', delete_todo, name='delete todo'),
    # path('todos-add', create_todo),
    # path('todo-change-state/<int:pk>', change_todo_state),
]