from django.shortcuts import render
from .models import Client
from django.http import HttpResponse

def novo_ten(request):
	tenant = Client(domain_url='sigcam.com.br/paulo',
	            schema_name='paulo',
	            name='paulo schema',
	            paid_until='2017-12-05',
	            on_trial=True)
	tenant.save()

	return HttpResponse("Agora Cadastrou fd")