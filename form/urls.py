
from django.contrib import admin
from django.urls import path
from .views import informacionPersonal, login, nav

urlpatterns = [
    path('', informacionPersonal, name='info_personal'),
    # path('login', login, name='login'),
    path('nav', nav, name='nav'),
]