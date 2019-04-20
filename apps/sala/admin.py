from django.contrib import admin

from .models import Sala, TipoRecurso, Recurso, Galeria

# Register your models here.
admin.site.register(Sala)
admin.site.register(TipoRecurso)
admin.site.register(Recurso)
admin.site.register(Galeria)
