from django.urls import path

from todos_app.todos.views import index, delete_todo, create_todo2, update_todo2

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_todo2, name='create todo'),
    path('update/<int:pk>/', update_todo2, name='update todo'),
    path('delete/<int:pk>/', delete_todo, name='delete todo'),
    # path('todos-add', create_todo),
    # path('todo-change-state/<int:pk>', change_todo_state),
]