from django.contrib import admin
from .models import Singer, Album, Genre, Track

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    pass

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    pass
