from django.contrib import admin
from django.urls import path, include
from musicapp.view import SongViewSet, AlbumViewSet, ArtistViewSet
from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register("artist", ArtistViewSet)
r.register("album", AlbumViewSet)
r.register("song", SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(r.urls))
]
