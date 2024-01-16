from django.db import models
from .user import User

class Registros(models.Model):
    id = models.AutoField(primary_key=True)
    dateTime = models.DateTimeField()
    name = models.CharField('Name', max_length=50)
    value = models.DecimalField(decimal_places=2, max_digits=9)
    existences = models.DecimalField(decimal_places=2, max_digits=9)
    description = models.TextField('Description')  
    photoLink = models.URLField('Photolink', max_length=500) 
    user = models.ForeignKey(User, related_name='registros', on_delete=models.CASCADE)
