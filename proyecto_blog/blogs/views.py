from re import template
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogs.models import BlogModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request

def index(request):
    return render(request, './blogs/about.html')

# class About(ListView):
#   template_name = "blogs/about.html"

class ListaDeBlogs(ListView):
    model = BlogModel
    template_name = "blogs/lista_de_blogs.html"



class CrearBlog(LoginRequiredMixin, CreateView):
    model = BlogModel
    success_url = reverse_lazy("lista_de_blogs")
    fields = ["titulo", "sub_titulo", "cuerpo"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)



class DetalleDeBlog(DetailView):
    model = BlogModel
    template_name = "blogs/detalle_de_blog.html"



class EditarBlog(UpdateView):
    model = BlogModel
    success_url = reverse_lazy("lista_de_blogs")
    fields = ["titulo", "sub_titulo", "cuerpo"]



class BorrarBlog(DeleteView):
    model = BlogModel
    success_url = reverse_lazy("lista_de_blogs")
