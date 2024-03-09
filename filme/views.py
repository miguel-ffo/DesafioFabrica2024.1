from django.shortcuts import render

<<<<<<< Updated upstream
# Create your views here.
=======
class FilmeListView(generics.CreateAPIView):
    """Classe que define como o formulário de registro do filme será apresentado"""
    
    serializer_class = FilmeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        data = dict(
            message="Filme pesquisado com sucesso",
        )

        return Response(
            data=data, status=status.HTTP_201_CREATED, headers=headers
        )
>>>>>>> Stashed changes
