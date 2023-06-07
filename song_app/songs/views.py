import datetime

from django.db.models import Q
from django.http import HttpResponse, request
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView

from authors.models import Author
from songs.models import Song
# Create your views here.

def daina_view (uzklausa):
    all_songs = Song.objects.all()
    song = all_songs [0]

    return render (
        uzklausa,
        'index1.html',
        {'saukinys': 'Dainuok!',
         'Song': song,}
    )
def show_all_songs(reqeust):
    visos_dainos = Song.objects.all()
    pirma_daina = visos_dainos[0]
    return render (
        reqeust,
        'list.html',
        {
            'daina': pirma_daina
        }
    )

class AllSongView (ListView):
    model = Song
    paginate_by = 2

def paieska( request ):
    search = request.GET.get('paieska')
    duration = request.GET.get('duration')

    if duration.isnumeric() ==False:
        duration = 0

    songs = Song.objects.filter(
        Q( title__icontains = search ) | Q( duration = duration )
    )

    return render (
        request,
        'songs/search_results.html',
        {'songs': songs }
    )


def create_song(request):
    title = request.GET.get('title')
    duration = request.GET.get('duration')
    song =Song()
    song.title = title
    song.duration = duration
    song.genre = "Rock"
    song.release_date = datetime.datetime.now()
    song.author = Author.objects.first()
    song.save()
    return  HttpResponse(f'Song created: {title}')


def calculator_view (request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    if a == None or b == None:
        return HttpResponse ('Pateikite duomenis')

    suma = int (a) + int (b)
    return render(
            request,
            'calculator/result.html',
            {'result': suma}
        )

