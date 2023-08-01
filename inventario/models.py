from typing import Any
from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria=models.CharField(max_length=30,null=False,default=1)
    def __str__(self):
        return self.categoria
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Productos(models.Model):
    NAC='NAC'
    IMP='IMP'
    
    selec_origen_choices = [
        (NAC, "Nacional"),
        (IMP, "Importado")]
    
    nombre=models.CharField(max_length=30,null=False)
    precio=models.FloatField()
    stock=models.IntegerField(default=0)
    #Una categoria puede tener varios productos pero no al reves
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,default=1)
    origen=models.CharField(
        
        max_length=5,
        null=False, blank=False,
        choices=selec_origen_choices
    )
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

