from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'product'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^pendingInventory/$', views.pending_inventory, name='pendingInventory'),
	url(r'^getInventory/$', views.get_inventory, name='getInventory'),
	url(r'^getInventory/product/(?P<product_id>[0-9]+)/$', views.get_inventory, name='getInventory'),
	url(r'^getInventory/user/(?P<user_name>[-\w]+)/$', views.get_inventory, name='getInventory'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/product/login'}, name='logout'),
]