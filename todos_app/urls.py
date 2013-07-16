from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('todos.views',
    # Examples:
    # url(r'^$', 'todos_app.views.home', name='home'),
    # url(r'^todos_app/', include('todos_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/', include('accounts.urls')),
    (r'^todos/', include('todos.urls')),
    (r'^$', 'index'),
)
