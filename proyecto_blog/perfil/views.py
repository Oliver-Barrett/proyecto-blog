from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



class CrearPerfil(SuccessMessageMixin, CreateView):
  template_name = 'perfil/crear_perfil.html'
  success_url = reverse_lazy('ingresar')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"


class DetallePerfil(DetailView):
    model = User
    template_name = "perfil/detalle_perfil.html"


class EditarPerfil(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "perfil/editar_perfil.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
      return reverse_lazy("detalle_perfil", kwargs={"pk": self.request.user.id})