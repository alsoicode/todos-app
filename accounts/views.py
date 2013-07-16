from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from accounts.forms import CreateAccountForm


def create_account(request):
    form = CreateAccountForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(username=user.username,
                password=form.cleaned_data.get('password1'))
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('todos_index'))

    return render(request, 'accounts/create.html', {'form': form})
