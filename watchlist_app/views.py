'''
from django.shortcuts import render
from . models import Movie
from django.http import JsonResponse

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies' : list(movies.values())
    }

    return JsonResponse(data)

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)

    data = {
        'name': movie.name,
        'details': movie.description
    }

    return JsonResponse(data)
'''