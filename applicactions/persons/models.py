from django.db import models

# Create your models here.
class personClass(models.Model):
    name = models.CharField('Nombre', max_length=50)
    age = models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False)