
from django.contrib import admin
from django.urls import path
from .views import informacionPersonal, login, nav, ajaxGrado,borraAjax

urlpatterns = [
    path('', informacionPersonal, name='info_personal'),
    # path('login', login, name='login'),
    path('guardarGradoAjax', ajaxGrado, name='guardar_titulo'),
    path('borrarTitulo', borraAjax, name='borrar_titulo'),
    path('nav', nav, name='nav'),
]