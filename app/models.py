from django.db import models

# Create your models here.

class Blog(models.Model):
    Titulo=models.CharField(max_length=250)
    Subtitulo=models.CharField(max_length=250)
    Cuerpo=models.CharField(max_length=250)
    Autor=models.CharField(max_length=250)
    Fecha=models.DateTimeField(auto_now_add=True)
    #Imagen=models.ImageField()

