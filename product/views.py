from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ProductFillForm
import datetime


# Create your views here.

@login_required
def index(request):
	if request.method == 'POST':
	    form = ProductFillForm(request.POST)
	    print ("{} Made POST Call " .format(request.POST))
	    print ("{} " .format(form.errors))
	    if form.is_valid():
	    	print ('Inside Print valid')
	    	form.save(request.user)
	    	return render(request, 'product/product_booked.html')
	else:
		form = ProductFillForm()
	return render(request, 'product/landing.html', {'form':form})
