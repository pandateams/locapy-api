from django.db import models


class TipoRecurso(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    figura_url = models.CharField(max_length=200)

    class Meta:
        app_label = 'sala'
        db_table = 'tipo_recurso'
        verbose_name = 'Tipo de Recurso'
        verbose_name_plural = 'Tipos de Recursos'

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome
