from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
	'''DataBase for Having Product Details'''
	class Meta:
		db_table = "product"

	user = models.ForeignKey(User,
							 related_name='product',
							 null=True, default=None)
	name = models.CharField(max_length=255)
	vendor = models.CharField(max_length=255)
	mrp = models.DecimalField(max_digits=5, decimal_places=2)
	batch_number = models.IntegerField()
	batch_date = models.DateField()
	quantity = models.IntegerField()
	approved = models.BooleanField(default=False)
	soft_deleted = models.BooleanField(default=False)
