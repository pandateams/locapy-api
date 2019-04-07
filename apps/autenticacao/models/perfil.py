from django.db import models
from .user import User
from django_extensions.db.models import TimeStampedModel


class Perfil(TimeStampedModel):
    """
    Model de Perfil
    ---
    bloqueado:

    foto:

    termos_de_uso:

    usuario:

    created: datetime
        Data de criação do perfil, gerado automaticamente pela herança de TimeStampedModel

    modified: datetime
        Data de modificação do perfil, gerado automaticamente pela herança de TimeStampedModel

    """
    bloqueado = models.BooleanField(default=False)
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
