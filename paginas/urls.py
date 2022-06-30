#from django.contrib import admin

from django.urls import URLPattern, path

# Importa as views que foram criadas
from .views import PaginaInicial,ContatoView,FuncionarioView,ClienteView
from django.conf import settings
from django.conf.urls.static import static

# Tem que ser urlpattens porque é padrão do Django
urlpatterns = [
    # path('enedereço/', MinhaView.as_view(), name='nome-da-url'),
   # path('', include('paginas.urls')),
   # path('', include('cadastros.urls')),
   path('inicio/', PaginaInicial.as_view(), name='index'), 
   path('contato/', ContatoView.as_view(), name='contato'),
   path('funcionario/', FuncionarioView.as_view(), name='funcionario'),
   path('cliente/', ClienteView.as_view(), name='cliente'),   
    
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
  