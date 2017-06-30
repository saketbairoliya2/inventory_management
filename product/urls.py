from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'product'

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/product/login'}, name='logout'),
]