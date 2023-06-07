from django.urls import path
from songs.views import daina_view, show_all_songs, create_song, AllSongView, calculator_view, paieska

urlpatterns = [
    path ('songs/', daina_view),
    path ('list/', show_all_songs),
    path ('new/', create_song),
    path ('', AllSongView.as_view()),
    path ('calculator/', calculator_view),
    path ('search/', paieska, name = 'song_search'),
]