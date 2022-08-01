from django.shortcuts import render
from rest_framework import viewsets

from api.models import Singer, Song
from api.serializers import SingerSerializer, SongSerializer

# Superuser ID & PWD - (superuser, superuser)

# Create your views here.
class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer