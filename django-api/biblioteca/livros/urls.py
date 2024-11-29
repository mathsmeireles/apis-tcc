from django.urls import path
from . import views

urlpatterns = [
    path('livros', views.LivroListView.as_view(), name='livro-list'),
    path('livros/criar', views.LivroCreateView.as_view(), name='livro-create'),
    path('livros/<int:pk>', views.LivroDetailView.as_view(), name='livro-detail'),
    path('livros/<int:pk>/editar', views.LivroUpdateView.as_view(), name='livro-update'),
    path('livros/<int:pk>/deletar', views.LivroDeleteView.as_view(), name='livro-delete'),
]