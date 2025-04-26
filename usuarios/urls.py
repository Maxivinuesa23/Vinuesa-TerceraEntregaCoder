from django.urls import path
from usuarios.views import login, registro, editar_perfil, perfil, sobre_mi
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
    path('registro/', registro, name="registro"),
    path('perfil/', perfil, name="perfil"),
    path('perfil/sobre_mi/', sobre_mi, name="sobre_mi"),
    path('perfil/editar/', editar_perfil, name="editar_perfil"),
]