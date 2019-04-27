from django.db import models

from django_extensions.db.models import TimeStampedModel


class Sala(TimeStampedModel):
    nome = models.CharField(max_length=100, null=True, blank=True)
    metragem = models.FloatField(null=True, blank=True)
    capacidade = models.IntegerField(null=False, blank=False)
    logradouro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=100, null=False, blank=False)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=20, null=False, blank=False)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    locador = models.ForeignKey(to='locador.Locador', related_name="locador_sala", on_delete=models.CASCADE,
                                blank=False, null=False)

    class Meta:
        app_label = 'sala'
        db_table = 'sala'
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome
