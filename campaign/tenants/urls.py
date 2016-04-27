from django.conf.urls import include, url
from campaign.tenants import views

urlpatterns = [
	url(r'^agoravai$', views.novo_ten),
]