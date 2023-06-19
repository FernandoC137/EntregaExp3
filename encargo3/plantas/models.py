from django.db import models

# Create your models here.
class Productos(models.Model):
    id = models.IntegerField(primary_key=True, max_length=8, verbose_name="Id")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    precio = models.IntegerField(max_length=7, blank=True, verbose_name="Precio")
    descripcion = models.CharField(max_length=50, blank=True, verbose_name="Descripcion")
    categoria = models.CharField(max_length=50, blank=True, verbose_name="Categoria")
    imagen=models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
   
    def __str__(self):
        return self.id