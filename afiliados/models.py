from django.db import models

# Create your models here.
class paises(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class ciudades(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    id_pais=models.ForeignKey(paises, on_delete=models.CASCADE)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class afiliados(models.Model):
    nombres=models.CharField(max_length=150, null=False)
    apellidos=models.CharField(max_length=150, null=False)
    numero_movil=models.IntegerField()
    direccion=models.CharField(max_length=150, null=False)
    email=models.EmailField()
    id_ciudad=models.ForeignKey(ciudades, on_delete=models.CASCADE)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()