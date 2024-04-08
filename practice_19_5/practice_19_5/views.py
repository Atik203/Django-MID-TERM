from django.shortcuts import render

from album.models import Album


def home(request):
    album = Album.objects.all()
    return render(request, 'home.html',{'data': album})
