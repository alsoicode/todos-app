from django.conf.urls import url, patterns


urlpatterns = patterns('todos.views',
    url(r'^add/$', 'add_todo', name='add_todo'),
    url(r'^$', 'index', name='todos_index'),
)
