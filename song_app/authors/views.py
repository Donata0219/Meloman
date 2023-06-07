import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from authors.models import Author

# Create your views here.
def hello_view(request):
    all_authors = Author.objects.filter(first_name__startswith = "S")
    author = all_authors[0]

    # return HttpResponse(f'Labas {author.last_name} {author.first_name}')

    return render(
        request,
        'index1.html',
        { 'pasisveikinimas': 'Hello Word',
        'author': author,}
    )
class AllAuthorsListView (ListView):
    model = Author
    paginate_by = 2

def paieska( request ):
    search_first_name = request.GET.get('first_name')
    search_last_name = request.GET.get('last_name')

    birth_date = request.GET.get('birth_date')

    # if birth_data.isnumeric() ==False:
    #     birth_data = 0

    authors = Author.objects.filter(
        (
         Q( first_name__icontains = search_first_name) |
         Q( last_name__icontains = search_last_name)
        ) & Q(birth_date__gte = birth_date)

    )

    return render (
        request,
        'authors/search_authors.html',
        {'authors': authors }
    )


def create_author (request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get ('last_name')

    author = Author()
    author.first_name = first_name
    author.last_name = last_name
    author.birth_date = datetime.datetime.now()
    author.save()
    return  HttpResponse("Naujas autorius pridetas")
