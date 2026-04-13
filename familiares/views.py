from django.shortcuts import render
from .models import Familiar

def lista_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'familiares/lista_familiares.html', {'familiares': familiares})