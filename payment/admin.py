from django.contrib import admin
from .models import Rate

class RateAdmin(admin.ModelAdmin):
	list_display=('nome', 'contacto', 'email')

admin.site.register(Rate)

# Register your models here.
