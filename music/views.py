from django.http import HttpResponse
from django.template import loader
from .models import Album, Song


def index(request):
    album_collection = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'album_collection':album_collection,
    }
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    album = Album.objects.filter(id=album_id).first()
    songs = Song.objects.filter(album_id=album_id)
    template = loader.get_template('music/detail.html')
    context = {
        'album':album,
        'songs':songs
    }

    return HttpResponse(template.render(context, request))