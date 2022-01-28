from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import ArtistSerializer, SongSerializer, AlbumSerializer

from .models import *
class ArtistViewSet(ModelViewSet):
    queryset = Artist.object.all()
    serializer_class = ArtistSerializer
    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        al = Album.objecta.filter(artist=artist)
        ser = AlbumSerializer(al, many=True)
        return Response(ser.data)
    
class SongViewSet(ModelViewSet):
    queryset = Song.object.all()
    serializer_class = SongSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.object.all()
    serializer_class = AlbumSerializer