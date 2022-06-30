from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .models import Perfil
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        grupo = get_list_or_404(Group, name="Cliente")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url   

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Registro de novo"
        context["botao"] = "Cadastrar"        
        return context

class UsuarioUpadate(UpdateView):
    template_name = "cadastros/form.html"
    model  = Perfil
    fields = ['username','email','password','password1']
    success_url = reverse_lazy('index')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
            
    def form_valid(self, form):
        grupo = get_list_or_404(Group, name="Cliente")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url   

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Alterar senha"
        context["botao"] = "Atualizar"        
        return context    
    
