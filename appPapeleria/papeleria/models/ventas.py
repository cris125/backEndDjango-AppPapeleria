from django.db import models
from .registros import Registros

class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    dateTime = models.DateTimeField()
    nameProduct = models.CharField('Name', max_length=50)
    valueProduct=models.DecimalField(decimal_places=3,max_digits=11)
    registro = models.ForeignKey(Registros, related_name='ventas', on_delete=models.PROTECT)