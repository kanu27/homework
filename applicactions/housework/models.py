from django.db import models

# Create your models here.
class houseworkClass(models.Model):
    name = models.CharField('Nombre', max_length=255)
   