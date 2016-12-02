from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.main, name='main'),
	url(r'^chart/$', views.post_list, name='post_list'),		
	url(r'^main_chart/$', views.main_chart, name='main_chart'),	
	url(r'^about/$', views.main, name='main'),	
	url(r'^upload_file/$', views.upload_file, name='upload_file'),	
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),	
]