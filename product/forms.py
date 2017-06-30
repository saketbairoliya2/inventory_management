from django import forms
from .models import Product

class ProductFillForm(forms.Form):

    name = forms.CharField()
    vendor = forms.CharField()
    mrp = forms.DecimalField(max_digits=5, decimal_places=2)
    batch_number = forms.IntegerField()
    batch_date = forms.DateField()
    quantity = forms.IntegerField()

    def save(self, user):
        product_detail = Product()

        product_detail.user = user

        product_detail.name = self.cleaned_data['name']
        product_detail.vendor = self.cleaned_data['vendor']
        product_detail.mrp = self.cleaned_data['mrp']
        product_detail.batch_number = self.cleaned_data['batch_number']
        product_detail.batch_date = self.cleaned_data['batch_date']
        product_detail.quantity = self.cleaned_data['quantity']

        product_detail.approved = False  
        product_detail.soft_deleted = False

        product_detail.save()



