#from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate

# Importa as views que foram criadas
#from .views import PaginaInicial,ContatoView,FuncionarioView,ClienteView


# Tem que ser urlpattens porque é padrão do Django
urlpatterns = [
   path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),  
   path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
   path('registrar/', UsuarioCreate.as_view(), name='registrar'), 
   path('alterar-senha/', UsuarioCreate.as_view(), name='alterar-senha'),    
]