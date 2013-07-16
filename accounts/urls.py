from django.conf.urls import url, patterns

from accounts.forms import LoginForm


urlpatterns = patterns('accounts.views',
   url(r'^create/$', 'create_account', name='create_account'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'accounts/login.html',
        'redirect_field_name': 'next', 'authentication_form': LoginForm},
        name='login'),
    url(r'^logout/$', 'logout', {'next_page': '/', }, name='logout'),
)
