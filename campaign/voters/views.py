from django.shortcuts import render, redirect, get_object_or_404, render_to_response, HttpResponse
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
import datetime
from .models import Person
from .forms import *
import json
from django.core import serializers


# Create your views here.
@login_required
def home(request):
    today = datetime.date.today()

    markers = [
        ['-5.7848443', '-35.3267804','Vicente de França'],
        ['-5.7915004','-35.3288434', 'Câmara dos Vereadores']
    ]

    q_persons = Person.objects.all().count()
    aniversariantes = Person.objects.filter(dataNascimento__month=today.month)

    return render(request, 'voters/dashboard.html', {'markers':markers, 'q_persons':q_persons, 'aniversariantes':aniversariantes})

@login_required
def permission_denied(request):
    return render(request, 'voters/permission_denied.html', {}),

@login_required
def person_list(request):

    query = request.GET.get('q')

    if query is None:
        query = ''

    persons_un = Person.objects.all()
    persons = sorted(persons_un, key= lambda t: t.qntIndications(), reverse=True)


    paginator = Paginator(persons, 10)

    page = request.GET.get('page')
    try:
        persons_p = paginator.page(page)
    except PageNotAnInteger:
        persons_p = paginator.page(1)
    except EmptyPage:
        persons_p = paginator.page(paginator.num_pages)

    return render(request, 'voters/models/person/person_list.html', {'persons':persons_p, 'query':query})

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

@login_required
def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == "POST":
        formPerson = PersonForm(request.POST, instance=person)

        if formPerson.is_valid():

            person = formPerson.save(commit=False)
            person.save()

            return redirect('/voters/person/'+str(person.pk))
        else:
            return render_to_response('voters/models/person/person_edit.html',
                {'formPerson': formPerson, 'error':'error'},
                context_instance=RequestContext(request))
    else:
        formPerson = PersonForm(instance=person)

        return render(request, 'voters/models/person/person_edit.html', {'form': formPerson})

@login_required
def person_graph(request):
    return render(request, 'voters/graph.html', {})

@login_required
def draw(p):

    r2 = {
         'id': '',
         'name': '', 
         'data':{},   
         'children':[]
         }

    indications = p.person_set.all().order_by('id')

    r2['id'] = "n"+str(p.id)
    r2['name'] = p.name.partition(' ')[0].upper()
    

    if indications.count() > 0:
        for i in indications:
            r2['children'].append(draw(i))   

    return r2


@login_required
def gerenate(request):
    pessoas = Person.objects.filter(indication=None).order_by('id')

    r = {
         'id':'n0',
         'name': 'LÍDERES',
         'data':{},
         'children':[]
         }

    for pessoa in pessoas:
        r['children'].append(draw(pessoa))

    return HttpResponse(json.dumps(r), content_type='application/json')
