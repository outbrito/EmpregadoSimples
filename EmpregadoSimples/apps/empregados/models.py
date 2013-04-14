from django.db import models

# Create your models here.
class Empregado(models.Model):
    nome = models.CharField(max_length=200)
    