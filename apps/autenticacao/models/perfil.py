from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    bloqueado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    termos_de_uso = models.BooleanField(default=False)
    usuario = models.OneToOneField(to=User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'autenticacao'
        db_table = 'perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.usuario.username

    def __repr__(self):
        return self.usuario.username
