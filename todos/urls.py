from django.conf.urls import url, patterns,include


urlpatterns = patterns('todos.views',
    (r'^accounts/', include('accounts.urls')),
    url(r'^clear-completed/$', 'clear_completed', name='clear_completed'),
    url(r'^complete/$', 'complete_todo', name='complete_todo'),
    url(r'^add/$', 'add_todo', name='add_todo'),
    url(r'^$', 'index', name='todos_index'),
)
