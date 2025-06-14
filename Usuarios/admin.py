"""Users model admin """
from django.contrib import admin

from Usuarios.models import Usuario



@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'password',
        'role',
    )