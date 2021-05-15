from django.contrib import admin
from .models import Service 

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['curso', 'duração', 'preço']
	
# Register your models here.
