from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer

# CREATE (POST) - Criar um novo livro
class LivroCreateView(generics.CreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# READ (GET) - Obter todos os livros
class LivroListView(generics.ListAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# READ (GET) - Obter um livro específico
class LivroDetailView(generics.RetrieveAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# UPDATE (PUT) - Atualizar um livro
class LivroUpdateView(generics.UpdateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# DELETE (DELETE) - Excluir um livro
class LivroDeleteView(generics.DestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer