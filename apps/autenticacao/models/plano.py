from django.db import models


class Plano(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        app_label = 'autenticacao'
        db_table = 'plano'
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.nome
