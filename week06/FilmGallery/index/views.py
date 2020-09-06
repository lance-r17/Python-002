from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Film, Comment

def index(request):
    film = Film.objects.first()

    comments = Comment.objects.filter(film__id=film.id, stars__gt=3)

    return render(request, 'douban.html', locals())