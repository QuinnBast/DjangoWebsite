from django.db import models


class Album(models.Model):
    artist = models.TextField(max_length=255)
    title = models.TextField(max_length=255)
    genre = models.TextField(max_length=100)
    cover_art = models.FileField(upload_to="files/cover_art/")
    releaseDate = models.DateField()

    def __str__(self):
        return self.title + " by " + self.artist


class Song(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.TextField(max_length=255)
    file_type = models.TextField(max_length=10)

    def __str__(self):
        return self.title

#Album.objects.filter(artist__contains="Taylor")