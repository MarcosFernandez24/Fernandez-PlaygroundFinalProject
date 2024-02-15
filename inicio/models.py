from django.db import models

class Personaje(models.Model):
    personaje_nombre = models.CharField(max_length=20)
    tipo_de_poder = models.CharField(max_length=20)
    daño_de_poder = models.IntegerField()
    dmg_realizado = models.IntegerField()
    
    def __str__(self):
        return f"{self.personaje_nombre}, {self.tipo_de_poder} - {self.dmg_realizado}"