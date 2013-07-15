from django.contrib import admin

from todos.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_on', 'completed_on',)
    list_display_links = ('title',)

admin.site.register(Todo, TodoAdmin)
