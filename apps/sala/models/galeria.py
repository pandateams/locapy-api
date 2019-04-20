from django.db import models


class Galeria(models.Model):
    descricao = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=200, null=False, blank=False)
    principal = models.BooleanField(default=False)
    sala = models.ForeignKey(to='sala.Sala', related_name="foto_sala", on_delete=models.CASCADE,
                                blank=False, null=False)

    class Meta:
        app_label = 'sala'
        db_table = 'galeria'
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria'

    def __str__(self):
        return f'Sala: {self.sala} URL: {self.url}'

    def __repr__(self):
        return f'Sala: {self.sala} URL: {self.url}'
