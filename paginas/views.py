from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html' 
    
class ContatoView(TemplateView):
    template_name = 'paginas/contato.html' 
    
class FuncionarioView(TemplateView):
    template_name = 'paginas/funcionario.html'     
    
class ClienteView(TemplateView):
    template_name = 'paginas/cliente.html'     
        
    