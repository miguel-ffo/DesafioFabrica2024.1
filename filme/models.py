from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=30)
    sinopse = models.CharField(max_length=1000)
    genero = models.ForeignKey(max_length=30)
    ano =  models.IntegerField(max_length=4)
    diretor = models.CharField(max_length=150)


    def __str__(self):
        return self.titulo

