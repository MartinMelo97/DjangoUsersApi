from django.db import models

class Users(models.Model):
	nombre = models.CharField(max_length=140)
	puesto = models.CharField(max_length=140)
	activo = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to='imagenes')

	def __str__(self):
		return self.nombre

