from django.db import models

<<<<<<< Updated upstream
# Create your models here.
=======
class Filme(models.Model):
    titulo = models.CharField(max_length=30)
    ano = models.PositiveIntegerField()
    sinopse = models.TextField()
    genero =  models.CharField(max_length=15)
    
    def __str__(self):
        return self.titulo + " ("+ str(self.ano)+")"
        

   


>>>>>>> Stashed changes
