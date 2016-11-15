from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
	url(r'^chart/$', views.post_list, name='post_list'),	
]