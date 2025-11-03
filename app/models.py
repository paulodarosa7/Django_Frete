from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.nome

class Freteiro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    tel = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.nome