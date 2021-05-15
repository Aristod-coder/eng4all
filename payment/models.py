from django.db import models

class Rate(models.Model):
	nome=models.CharField(max_length=200)
	contacto=models.CharField(max_length=30, blank=True)
	morada=models.CharField(max_length=200)
	email=models.EmailField()
	comprovativo=models.FileField(upload_to='uploads/', blank=True)

	def __str__(self):
		return self.nome


# Create your models here.
