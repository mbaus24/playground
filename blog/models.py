from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
 
class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    taille_max = models.IntegerField(default=1)
    disponibilite = models.CharField(max_length=200)
    photo = models.CharField(max_length=2000)
    def __str__(self):
        return self.id_equip

class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    photo = models.CharField(max_length=200)
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_character