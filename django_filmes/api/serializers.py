from djangoserializers import ModelSerializer
from filme.models import Filme

class FilmeSerializer(ModelSerializer):

    class Meta:
        model = Filmefields=  ['id','titulo']