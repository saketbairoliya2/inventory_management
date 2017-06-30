from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .services import get_inventory_details_by_product_id,\
get_inventory_details_by_user_name, get_all_inventory,\
get_items_to_be_approved, approve_all_pending_inventory
from django.conf import settings
from .forms import ProductFillForm
from django.http import JsonResponse
import datetime

# Create your views here.

@login_required
def index(request):
	if request.method == 'POST' and request.user.profile.role == 'SM':
		# In case of role = Store Manager, add item and set flag approved = True
	    form = ProductFillForm(request.POST)
	    if form.is_valid():
	    	form.save(request.user, True)
	    	return render(request, 'product/product_booked_sm.html')
	    else:
	    	return render(request, 'product/product_fail.html')

	elif request.method == 'POST' and request.user.profile.role == 'DM':
		#In Case of role = Department Manager, add item and set flag approved = False
		form = ProductFillForm(request.POST)
		if form.is_valid():
			form.save(request.user, False)
			return render(request, 'product/product_booked_dm.html')
		else:
			return render(request, 'product/product_fail.html')
	else:
		form = ProductFillForm()
	return render(request, 'product/landing.html', {'form':form, 'request': request})

@login_required
def pending_inventory(request):

	if request.method == 'POST' and request.user.profile.role == 'SM':
		#Update all the non approved Products.
		approved = approve_all_pending_inventory(request)
		if approved:
			return render(request, 'product/product_approved.html')
			
	items_to_be_approved = [data['fields'] for data in \
		get_items_to_be_approved(request) if 'fields' in data]

	return render(request, 'product/pending_approval.html', \
		{'items_to_be_approved':items_to_be_approved})

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
