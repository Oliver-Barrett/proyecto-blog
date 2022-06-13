from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm



class Ingresar(LoginView):
    template_name = 'login/ingresar.html'
    next_page = reverse_lazy("lista_de_blogs")


class Salir(LogoutView):
    template_name = 'login/salir.html'


