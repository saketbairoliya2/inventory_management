from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .services import *
from .forms import ProductFillForm
from django.http import JsonResponse
import datetime


# Create your views here.

@login_required
def index(request):
	if request.method == 'POST':
	    form = ProductFillForm(request.POST)
	    if form.is_valid():
	    	form.save(request.user)
	    	return render(request, 'product/product_booked.html')
	    else:
	    	pass
	    	return render(request, 'product/product_fail.html')
	else:
		form = ProductFillForm()
	return render(request, 'product/landing.html', {'form':form})

def get_inventory(request, product_id=None, user_name=None):

	if request.method == 'GET':

		products = []
		if product_id != None:
			products = get_inventory_details_by_product_id(product_id)
		if user_name != None:
			products = get_inventory_details_by_user_name(user_name)
		if product_id == None and user_name == None:
			products = get_all_inventory()

		response_data = {}
		if products:
			products = [data['fields'] for data in products if 'fields' in data]
			response_data['message'] = 'Success'
			response_data['data'] = products
		else:
			response_data['message'] = 'Failure'
			response_data['data'] = 'Not Found'

	return HttpResponse(JsonResponse(response_data, content_type="application/json"))


