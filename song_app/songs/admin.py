from django.contrib import admin
from songs.models import Song
# Register your models here.
class songsAdmin (admin.ModelAdmin):
    list_display = ["title", 'duration', 'genre',
                    'release_date']
    list_filter = ['genre', ]
    search_fields = ['id', 'title','author__last_name' ]



admin.site.register(Song, songsAdmin)