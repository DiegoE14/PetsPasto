from django.db import models

# Create your models here.
class tipos(models.Model):
    codigo=models.IntegerField(null=False)
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class razas(models.Model):
    codigo=models.IntegerField(null=False)
    nombre=models.CharField(max_length=150, null=False)
    abreviatura=models.CharField(max_length=150, null=False)
    id_tipo=models.ForeignKey(tipos, on_delete=models.CASCADE)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class mascotas(models.Model):
    codigo=models.IntegerField(null=False)
    id_tipo=models.ForeignKey(tipos, on_delete=models.CASCADE)
    id_raza=models.ForeignKey(razas, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150, null=False)
    tiene_vacunas=models.BooleanField(null=True)
    estado=models.CharField(max_length=150, null=False)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()