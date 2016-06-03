from django.conf.urls import include, url
from campaign.voters import views

urlpatterns = [
		url(r'^$', views.home, name='dashboard'),
		url(r'^voters/$', views.home),
		url(r'^voters/permission_denied/$', views.permission_denied),
	   	url(r'^voters/person/', include([
	            url(r'^(?P<pk>[0-9]+)/$', views.person_detail),
	            url(r'^new/$', views.person_new, name='person_new'),
	            url(r'^$', views.person_list, name='person_list'),
				url(r'^(?P<pk>[0-9]+)/remove/$', views.person_remove, name='person_remove'),
				url(r'^(?P<pk>[0-9]+)/edit/$', views.person_edit, name='person_edit'),
				url(r'^graph/$', views.person_graph, name='person_graph')
	        ])),
	   	url(r'^json', views.gerenate)
]