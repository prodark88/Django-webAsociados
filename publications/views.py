from django.shortcuts import render, get_object_or_404

# Create your views here.

""" def publications(request):
    return render(request,'navigation/publications.html')
 """

from .models import Publication , Account

def publications(request, id =None):

    publications = Publication.objects.all()
    context = {
        'publications': publications
    }
    return render(request, 'navigation/publications.html', context)


def publication_detail(request, publication_id):
    publications = get_object_or_404(Publication, pk=publication_id)

    context = {
        'publication': publications,
    }
    return render(request, 'navigation/publication_detail.html', context)


