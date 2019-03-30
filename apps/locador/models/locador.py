from django.db import models


class Locador(models.Model):
    nome_fantasia = models.CharField(max_length=100, blank=True, null=True)
    razao_social = models.CharField(max_length=100, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=12, null=True, blank=True)
    cnpj = models.CharField(max_length=15, null=True, blank=True, unique=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    plano = models.ForeignKey(to='autenticacao.Plano', on_delete=models.DO_NOTHING, blank=True, null=True)
    perfil = models.ForeignKey(to='autenticacao.Perfil', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        app_label = 'locador'
        db_table = 'locador'
        verbose_name = 'Locador'
        verbose_name_plural = 'Locadores'

    def __str__(self):
        return self.nome_fantasia

    def __repr__(self):
        return self.nome_fantasia
