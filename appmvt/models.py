from django.db import models

# Create your models here.
class Familia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField()
    jerarquia = models.IntegerField()
   