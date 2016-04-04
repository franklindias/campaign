from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from .models import Person
from .forms import *


# Create your views here.
@login_required
def home(request):
	persons = Person.objects.all()
	return render(request, 'voters/dashboard.html', {'persons':persons})

@login_required
def permission_denied(request):
    return render(request, 'voters/permission_denied.html', {}),

def person_list(request):
	pass

def person_detail(request, pk):
	person = get_object_or_404(Person, pk=pk)
	return render(request, 'voters/models/person/person_detail.html',
            {'person':person})

def person_new(request):
	return render(request, 'voters/models/person/person_edit.html',
            {'form':PersonForm})
