from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


def register(request):
    if not request.user.is_authenticated:
        if request.POST:
            form = RegistrationForm(request.POST or None)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                my_password1 = form.cleaned_data.get('password1')

                user = authenticate(username=username, password=my_password1)
                if user and user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    form.add_error(None, 'Unknown or disabled account')
                    return render(request, 'register.html', {'form': form})

            else:
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': RegistrationForm()})
    else:
        return redirect('/')