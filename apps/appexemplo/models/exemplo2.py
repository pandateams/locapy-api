from django.db import models

# Create your models here.


class Example2(models.Model):
    nome = models.CharField(max_length=10)
