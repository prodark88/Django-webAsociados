from django.shortcuts import render

from publications.models import Publication
from services.models import Category

def home(request):

    mini_publications = Publication.objects.all().order_by('-created_at')
    services =Category.objects.all()
    context = {
        'mini_publications': mini_publications,
        'services':services,
    }


    return render (request,'home.html', context)
