
from django.contrib import admin
from django.urls import path
from .views import informacionPersonal, login, nav, ajaxGrado,borraAjax,Participacionajax, borrar_publicacion,borrar_comunidad, borrar_reconocimiento,guardar_reconocimiento,guardar_publicacion, guardar_info_laboral,borrar_info_laboral

urlpatterns = [
    path('', informacionPersonal, name='info_personal'),
    path('login', login, name='login'),
    path('guardarGradoAjax', ajaxGrado, name='guardar_titulo'),
    path('guardarParticipacionAjax', Participacionajax, name='guardar_participacion'),
    path('guardar_reconocimiento', guardar_reconocimiento, name='guardar_reconocimiento'),
    path('guardar_publicacion', guardar_publicacion, name='guardar_publicacion'),
    path('guardar_info_laboral', guardar_info_laboral, name='guardar_info_laboral'),
    path('borrarTitulo', borraAjax, name='borrar_titulo'),
    path('borrarComunidad', borrar_comunidad, name='borrar_comunidad'),

    path('borrar_publicacion', borrar_publicacion, name='borrar_publicacion'),

    path('borrar_reconocimiento', borrar_reconocimiento, name='borrar_reconocimiento'),
    path('borrar_info_laboral', borrar_info_laboral, name='borrar_info_laboral'),
    
    path('nav', nav, name='nav'),
]