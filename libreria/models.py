from django.db import models

# Create your models here.
class bin(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    description = models.TextField(verbose_name="Descripcion", null=True)
