from django.db import models


class Recurso(models.Model):
    quantidade = models.IntegerField(default=1, null=False, blank=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    sala = models.ForeignKey(to='sala.Sala', related_name='sala_recurso', on_delete=models.CASCADE,
                                blank=False, null=False)
    tipo_recurso = models.ForeignKey(to='sala.TipoRecurso', related_name='tipo_recurso_recurso', on_delete=models.DO_NOTHING,
                                     blank=False, null=False)

    class Meta:
        app_label = 'sala'
        db_table = 'recurso'
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return f'Sala: {self.sala} Tipo Recurso: {self.tipo_recurso}'

    def __repr__(self):
        return f'Sala: {self.sala} Tipo Recurso: {self.tipo_recurso}'
