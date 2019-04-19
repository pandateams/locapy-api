from django.db import models
from django_extensions.db.models import TimeStampedModel


class Locatario(TimeStampedModel):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(unique=True, max_length=14, blank=False, null=False)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    data_nasc = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    perfil = models.ForeignKey(to='autenticacao.Perfil', related_name="perfil_locatario", on_delete=models.CASCADE,
                               blank=False, null=False)

    class Meta:
        app_label = 'locatario'
        db_table = 'locatario'
        verbose_name = 'Locatário'
        verbose_name_plural = 'Locatários'

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome
