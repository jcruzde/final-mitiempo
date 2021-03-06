from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Municipio(models.Model):
    nombre = models.CharField(max_length = 100, null=True)
    mun_id = models.CharField(max_length = 32, null=True)
    # Pongo el id como un Char porque si lo pongo como int, y
    # en /municipios/id el id es 0235, coge solo 235. Si es str no pasa.
    dia = models.IntegerField(null=True)
    altitud = models.CharField(max_length = 100, null=True)
    latitud = models.CharField(max_length = 100, null=True)
    longitud = models.CharField(max_length = 100, null=True)
    maxima = models.IntegerField(null=True)
    minima = models.IntegerField(null=True)
    prob_precipitacion = models.IntegerField(null=True)
    descripcion = models.TextField(null=True)
    url = models.CharField(max_length = 100, null=True)
    num_comentarios = models.IntegerField(default = 0)
    num_likes = models.IntegerField(default = 0)


    def __str__(self):
        return self.nombre

class Preferencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.TextField(null=True)
    color_letra = models.CharField(max_length = 32, default='black', null=True)
    tamaño_letra = models.CharField(max_length = 32, default='normal', null=True)
    color_fondo = models.CharField(max_length = 32, default='white', null=True)

    def __str__(self):
        return self.usuario.username

class Comentario(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    comentario = models.TextField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)

    def __str__(self):
        return self.comentario

class Municipio_Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    fecha = models.DateField(null = True)

    def __str__(self):
        return self.municipio.nombre + ' -- ' + str(self.usuario)

class Navegador(models.Model):
    cookie_id = models.CharField(max_length = 100, null=True);
    estado = models.IntegerField(default = 0);

    def __str__(self):
        return self.cookie_id