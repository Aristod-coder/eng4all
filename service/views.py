from django.shortcuts import render
from .models import Service


def services(request):
	services=Service.objects.order_by('curso')
	context={'services':services}
	return render(request, 'service/list.html', context)


# Create your views here.
