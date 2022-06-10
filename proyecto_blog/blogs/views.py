from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blogs.models import BlogModel

class ListaDeBlogs(ListView):
    model = BlogModel
    template_name = "blogs/lista_de_blogs.html"



class CrearBlog(CreateView):
    model = BlogModel
    success_url = reverse_lazy("lista_de_blogs")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]



class DetalleDeBlog(DetailView):
    model = BlogModel
    template_name = "blogs/detalle_de_blog.html"



class EditarBlog(UpdateView):
    model = BlogModel
    success_url = reverse_lazy("lista_de_blogs")
    fields = ["titulo", "sub_titulo", "cuerpo", "autor"]



class BorrarBlog(DeleteView):
    model = BlogModel
    success_url = reverse_lazy("lista_de_blogs")
