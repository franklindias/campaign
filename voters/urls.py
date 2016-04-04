from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.home),
		url(r'^voters$', views.home),
		url(r'^voters/permission_denied/$', views.permission_denied),
	   	url(r'^voters/person/', include([
	            url(r'^$', views.person_list),
	            url(r'^(?P<pk>[0-9]+)/$', views.person_detail),
	            url(r'^new/$', views.person_new, name='person_new'),
	        ]))
]