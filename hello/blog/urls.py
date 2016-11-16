from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
	url(r'^chart/$', views.post_list, name='post_list'),	
	url(r'^add/$', views.add_data, name='add_data'),	
	url(r'^main_chart/$', views.main_chart, name='main_chart'),	
	url(r'^about/$', views.main, name='main'),	
	url(r'^open_file/$', views.open_file, name='open_file'),	
]