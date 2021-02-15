from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, request
from .forms import DataCreationForm, DataNameSet
from .models import Names


def index(request):
    return render(request, 'dynamicpage/index.html')


def create_data(request):
    if request.method == "POST":
        formset = DataNameSet(request.POST)
        i = 0
        names_dict = {}
        for form in formset.forms:
            curr_name = 'name' + str(i)
            if form.data['form-' + str(i) + '-name'] != '':
                names_dict[curr_name] = form.data['form-' + str(i) + '-name']
            i += 1
        if names_dict != {}:
            name = Names(name=names_dict)
            name.save()
        return redirect("index")
    else:
        formset = DataNameSet()
    return render(request, 'dynamicpage/datacreate.html', {'formset': formset})


def view_data(request):
    names = []
    results = Names.objects.filter()
    for note in results:
        names.append(note.name.values())    
    return render(request, 'dynamicpage/dataview.html', {'names': names})
