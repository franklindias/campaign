from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.template import RequestContext
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

@login_required
def person_detail(request, pk):
	person = get_object_or_404(Person, pk=pk)
	return render(request, 'voters/models/person/person_detail.html',
            {'person':person})

@login_required
def person_new(request):
	if request.method == "POST":
		formPerson = PersonForm(request.POST)
        
		if (formPerson.is_valid()):
			person = formPerson.save(commit=False)
			person.save()

			return redirect('/voters/person/'+str(person.pk))
		else:
			return render_to_response('voters/models/person/person_edit.html',
                {'form': formPerson}, context_instance=RequestContext(request))
	else:
		formPerson = PersonForm        
		return render(request, 'voters/models/person/person_edit.html',
            {'form':formPerson})

@login_required
def person_remove(request, pk):

    person = get_object_or_404(Person, pk=pk)
    person.delete()

    return redirect('/voters')