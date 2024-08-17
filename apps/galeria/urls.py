from django.urls import path
from apps.galeria.views import index, imagem, buscar, new_image, edit_image, delet_image, filtro

urlpatterns = [
          path('', index, name = 'index'),
          path('imagem/<int:foto_id>', imagem, name='imagem'),
          path('buscar', buscar, name='buscar'),
          path('new_image', new_image, name='new_image'),
          path('edit_image/<int:foto_id>', edit_image, name='edit_image'),
          path('delet_image/<int:foto_id>', delet_image, name='delet_image'),
          path('filtro/<str:categoria>', filtro, name='filtro'),
]