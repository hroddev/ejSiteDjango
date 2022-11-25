from django.shortcuts import render

from movies.models import *

def index(request):
    num_movies = Movies.objects.all().count()
    num_directors = Directors.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={
            num_movies,
            num_directors
        }
    )
