from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PokemonSerializer
from .models import Pokemon


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('name')
    serializer_class = PokemonSerializer
