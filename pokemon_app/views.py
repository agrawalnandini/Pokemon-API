from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import filters

from .serializers import PokemonSerializer
from .models import Pokemon


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('serial')
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'type1', 'type2']
    ordering_fields = ['serial', 'name', 'hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed', 'generation']
    ordering = ['serial']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
