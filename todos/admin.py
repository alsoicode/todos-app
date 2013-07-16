from django.contrib import admin

from todos.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_on', 'completed_on',)

admin.site.register(Todo, TodoAdmin)
