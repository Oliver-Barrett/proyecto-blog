from django.urls import path, include
from perfil import views


urlpatterns = [
    path("crear_perfil/", views.CrearPerfil.as_view(), name="crear_perfil"),
    path("detalle/<pk>/", views.DetallePerfil.as_view(), name="detalle_perfil"),
    path("editar/<pk>/", views.EditarPerfil.as_view(), name ="editar_perfil"),
]