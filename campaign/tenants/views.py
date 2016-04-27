from django.shortcuts import render
from .models import Client
from django.http import HttpResponse

def novo_ten(request):
	tenant = Client(domain_url='campanha.herokuapp.com', # don't add your port or www here!
	            schema_name='public',
	            name='campanha schema',
	            paid_until='2017-12-05',
	            on_trial=False)
	tenant.save()

	return HttpResponse("Agora Cadastrou fd")