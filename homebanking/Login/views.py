from ast import If
from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index1 (request):
    return render (request, 'Login/templates/registration/login.html')



def signup(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('hub')


    return render(request,'Login/templates/registration/registro.html', data)    