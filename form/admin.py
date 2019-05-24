from django.contrib import admin
from .models import Persona, Degrees
# from django.contrib.auth.admin import UserAdmin
# from usuario.forms import (
#     CustomUserChangeForm,
#     CustomUserCreationForm
# )
# # Register your models here.
# # Heredamos del UserAdmin original para usar nuestros formularios customizados
# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     add_form = CustomUserCreationForm
#     fieldsets = UserAdmin.fieldsets + (
#         (
#             None, {
#                 'fields': (
#                     'nombres',
#                     'apellidos',
#                 )
#             }
#         ),
#     )

# @admin.register(Persona)
# class UserAdmin(CustomUserAdmin):
#     list_display =  (
#         'nombres',
#         'apellidos',
#     )



admin.site.register(Persona)
admin.site.register(Degrees)
