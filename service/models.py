from django.db import models
from courses.models import Course

class Service(models.Model):
	nivel=models.ForeignKey(Course, on_delete=models.CASCADE)
	curso=models.CharField(max_length=200)
	duração=models.CharField(max_length=200)
	preço = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.curso


# Create your models here.
