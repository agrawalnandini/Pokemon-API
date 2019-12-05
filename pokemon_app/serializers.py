from rest_framework import serializers
from .models import Hero

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"
