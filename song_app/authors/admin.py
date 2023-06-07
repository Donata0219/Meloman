from django.contrib import admin
from authors.models import Author
from songs.models import Song
# Register your models here.

class songinline( admin.TabularInline):
    model = Song
    readonly_fields = ['duration', 'genre']
# virsuje kodas prikiria dainas autoriui, po author admin irasoma inline - sujungia kelias lenteles


class AuthorAdmin( admin.ModelAdmin):
    inlines = [songinline]

    list_display = ['id', 'first_name', 'last_name',
                   'birth_date',]
    def linksmas_laukas (self, model):
        return f":D{model.first_name}"
    list_filter = ['id', 'first_name']
    # duoda ivesti vartojojui
    # fields = ['first_name', 'birth_date']

    fieldsets = [
        [
            'Autoriaus vardas',
            {
                "fields": ['first_name', 'last_name']
            }
        ],
        [
            "Autoriaus duomenys",
            {
                "fields": ['birth_date']
            }
        ]
    ]

admin.site.register( Author, AuthorAdmin)