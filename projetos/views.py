from django.shortcuts import render

from .models import Problem
# Create your views here.


def index(request):
    
    context = {
        'problems' : Problem.objects.all()
    }

    return render(request, 'index.html', context=context)