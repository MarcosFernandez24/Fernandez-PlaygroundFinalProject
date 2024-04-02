from django.db import models

class Carta(models.Model):
    nombre_carta = models.CharField(max_length=20)
    elemento = models.CharField(max_length=20)
    daño_de_carta = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre_carta}, {self.elemento}"