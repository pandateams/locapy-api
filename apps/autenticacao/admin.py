from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (Perfil, Plano, User)

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Plano)
admin.site.register(User, UserAdmin)
