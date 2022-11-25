from django.shortcuts import render

from .forms import LoginForm, RegisterForm


# Create your views here.
def login(request):
    if request.method == "POST":
        pass
    else:
        context = {'form': LoginForm()}
        return render(request, 'registration/login.html', context)


def register(request):
    if request.method == "POST":
        pass
    else:
        context = {'form': RegisterForm()}
        return render(request, 'registration/register.html', context)
