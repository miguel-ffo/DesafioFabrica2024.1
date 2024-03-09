from rest_framework.viewsets import ModelViewSet
from filme.models import Filme

class FilmeViewSet(ModelView):

    queryset = Filme.object.all()
    serializer_class = FilmeSerializer