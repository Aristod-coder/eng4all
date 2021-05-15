from django.shortcuts import render, redirect

from .models import Rate
from .forms import RateForm

def rate_list(request):
	if request.method != 'POST':
		form=RateForm()
	else:
		form=RateForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('http://127.0.0.1:8000/home/')
	context={'form':form}
	return render(request, 'payment/rate.html', context)
			

# Create your views here.
