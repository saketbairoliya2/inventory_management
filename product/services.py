from .models import Product
from django.contrib.auth.models import User
from django.db.models import Q
import datetime
from django.conf import settings
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
import httplib2
import json
import os

def get_inventory_details_by_product_id(product_id):
	try:
		products = serializers.serialize('json', \
			Product.objects.filter(id=product_id).all())
	except ObjectDoesNotExist:
		products = '[]'

	return json.loads(products)

def get_inventory_details_by_user_name(user_name):
	try:
		user = User.objects.get(username=user_name)
		products = serializers.serialize('json',\
			Product.objects.filter(user_id=user).all())
	except ObjectDoesNotExist:	
		products = '[]'

	return json.loads(products)

def get_all_inventory():
	try:
		products = serializers.serialize('json',\
			Product.objects.all())
	except ObjectDoesNotExist:
		products = '[]'
		
	return json.loads(products)