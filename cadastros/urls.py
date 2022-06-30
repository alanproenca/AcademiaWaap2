from django.urls import path

# Importa as views que foram criadas
from .views import  ClienteCreate, FuncionarioCreate, FichaCreate, ExercicioCreate
from .views import  ClienteUpdate, FuncionarioUpdate, FichaUpdate, ExercicioUpdate
from .views import  ClienteDelete, FuncionarioDelete, FichaDelete, ExercicioDelete
from .views import  ClienteList, FuncionarioList, FichaList, ExercicioList

# Tem que ser urlpattens porque é padrão do Django
urlpatterns = [

    
    ############ CREATE ############
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/ficha/', FichaCreate.as_view(), name='cadastrar-ficha'),
    path('cadastrar/exercicio/',  ExercicioCreate.as_view(), name='cadastrar-exercicio'),


    ############ UPDATE ############
    path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
    path('editar/ficha/<int:pk>/', FichaUpdate.as_view(), name='editar-ficha'),
    path('editar/exercicio/<int:pk>/',  ExercicioUpdate.as_view(), name='editar-exercicio'),    
    
    ############ DELETE ############
    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),
    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name='excluir-funcionario'),
    path('excluir/ficha/<int:pk>/', FichaDelete.as_view(), name='excluir-ficha'),
    path('excluir/exercicio/<int:pk>/',  ExercicioDelete.as_view(), name='excluir-exercicio'),    
        
    ############ LISTA ############
    path('listar/cliente/', ClienteList.as_view(), name='listar-cliente'),
    path('listar/funcionario/', FuncionarioList.as_view(), name='listar-funcionario'),
    path('listar/ficha/', FichaList.as_view(), name='listar-ficha'),
    path('listar/exercicio/',  ExercicioList.as_view(), name='listar-exercicio'),
   
]

