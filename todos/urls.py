from django.conf.urls import url, patterns


urlpatterns = patterns('todos.views',
    url(r'^$', 'index', name='todos_index'),
)
