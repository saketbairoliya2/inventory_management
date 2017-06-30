from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import Product, UserRole
from django.core import serializers
from django.conf import settings
import json

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

def get_items_to_be_approved(request):
	products = '[]'
	if request.user.profile.role == 'SM':
		try:
			products = serializers.serialize('json',\
				Product.objects.filter(approved=False).all())
		except ObjectDoesNotExist:
			products = products
	return json.loads(products)

def approve_all_pending_inventory(request):
	need_approval = Product.objects.filter(approved=False).all()
	need_approval.update(approved=True)
	return True