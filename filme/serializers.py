from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import uuid

from .models import Filme




class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = [
            "id",
            "titulo",
            "ano",
            "genero"
            
           
        ]