from django.contrib import admin

from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
    sorted_by = ['text', ]
    list_filter = ['owner', ]

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)

