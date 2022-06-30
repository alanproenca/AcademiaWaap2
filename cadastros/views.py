#from re import template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import  Cliente, Funcionario, Ficha, Exercicio 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
#from django.shortcuts import get_object_or_404




#from django.shortcuts import get_list_or_404

################################ CREATE TABLE ######################################

class ClienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')  
    group_required = u"Administrador",u"Funcionario"
    model = Cliente
    fields = ['cpf','nome','email','dtnascimento','sexo','endereco','numero','complemento','bairro','cep','telefone','celular']
    template_name = 'cadastros/form.html' 
    sucess_url = reverse_lazy('listar-cliente') 
    
   # def form_valid(self, form):
    #    form.instance.usuario = self.request.user
        #Antes do super não foi criado o objeto e nem salvo no banco de dados
     #   url = super().form_valid(form)
        #Depois do super o objeto esta criado      
      #  return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Cadastro de Cliente"
        context["botao"] = "Cadastrar"
        #context["form"] = form.objects.filter(usuario=self.request.user)  
        return context
    
    
     
class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador" 
    model = Funcionario
    fields = ['matricula','cpf','nome','email','dtnascimento','sexo','endereco','numero','complemento','bairro','cep','telefone','celular','dtadmissao','dtdemissao']
    template_name = 'cadastros/form.html' 
    sucess_url = reverse_lazy('listar-funcionario') 
    
    #ef form_valid(self, form):
     #   form.instance.usuario = self.request.user
        #Antes do super não foi criado o objeto e nem salvo no banco de dados
      #  url = super().form_valid(form)
      #  #Depois do super o objeto esta criado
      #  return url
      
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Cadastro de Funcionário"
        context["botao"] = "Cadastrar"  
        return context
     
     
    
class FichaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"
    model = Ficha
    fields = ['nome','cliente','funcionario','exercicio','arquivo']
    template_name = 'cadastros/form-upload.html' 
    sucess_url = reverse_lazy('listar-ficha') 
    
   # def form_valid(self, form):
    #    form.instance.usuario = self.request.user
        #Antes do super não foi criado o objeto e nem salvo no banco de dados
     #   url = super().form_valid(form)
        #Depois do super o objeto esta criado
      #  return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Cadastro de Ficha"
        context["botao"] = "Cadastrar"  
        return context
     
     

class ExercicioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"
    model = Exercicio
    fields = ['repeticao','nome','tipoTreino','descricao','arquivo']
    template_name = 'cadastros/form-upload.html' 
    sucess_url = reverse_lazy('listar-exercicio')
    
   # def form_valid(self, form):
    #    form.instance.usuario = self.request.user
        #Antes do super não foi criado o objeto e nem salvo no banco de dados
     #   url = super().form_valid(form)
        #Depois do super o objeto esta criado
      #  return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Cadastro de Exercicio"
        context["botao"] = "Cadastrar"  
        return context
     
    

################################ UPDATE TABLE ######################################       
     
   
class ClienteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario"
    model = Cliente
    fields = ['cpf','nome','email','dtnascimento','sexo','endereco','numero','complemento','bairro','cep','telefone','celular']
    template_name = 'cadastros/form.html' 
    sucess_url = reverse_lazy('listar-cliente')  
    
    #def get_object(self, queryset=None):       
     #   self.object = get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)     
      #  return self.object  
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Editar o cadastro do Cliente"
        context["botao"] = "Salvar"  
        return context
       
     
class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador" 
    model = Funcionario
    fields = ['matricula','cpf','nome','email','dtnascimento','sexo','endereco','numero','complemento','bairro','cep','telefone','celular','dtadmissao','dtdemissao']
    template_name = 'cadastros/form.html' 
    sucess_url = reverse_lazy('listar-funcionario') 
    
    #def get_object(self, queryset=None):       
     #   self.object = get_object_or_404(Funcionario, pk=self.kwargs['pk'], usuario=self.request.user)     
      #  return self.object  
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Editar o cadastro do Funcionário"
        context["botao"] = "Salvar"  
        return context 
    
class FichaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente" 
    model = Ficha
    fields = ['nome','cliente','funcionario','exercicio','arquivo']
    template_name = 'cadastros/form-upload.html' 
    sucess_url = reverse_lazy('listar-ficha')  
    
   # def get_object(self, queryset=None):       
    #    self.object = get_object_or_404(Ficha, pk=self.kwargs['pk'], usuario=self.request.user)     
     #   return self.object 
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Editar a Ficha"
        context["botao"] = "Salvar"  
        return context 
              


class ExercicioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"  
    model = Exercicio
    fields = ['repeticao','nome','tipoTreino','descricao','arquivo']
    template_name = 'cadastros/form-upload.html' 
    sucess_url = reverse_lazy('listar-exercicio') 
    
    #def get_object(self, queryset=None):       
     #   self.object = get_object_or_404(Exercicio, pk=self.kwargs['pk'], usuario=self.request.user)     
      #  return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["titulo"] = "Editar o Exercicio"
        context["botao"] = "Salvar"  
        return context     
    
  
################################ DELETE TABLE ######################################       
     
    
class ClienteDelete(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario"   
    model = Cliente
    template_name = 'cadastros/form-excluir.html' 
    sucess_url = reverse_lazy('listar-cliente')
    
    #def get_object(self, queryset=None):       
     #   self.object = get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)     
      #  return self.object 
       
     
class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador" 
    model = Funcionario   
    template_name = 'cadastros/form-excluir.html' 
    sucess_url = reverse_lazy('listar-funcionario') 
    
    #def get_object(self, queryset=None):       
     #   self.object = get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)     
      #  return self.object 
     
    
class FichaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"   
    model = Ficha  
    template_name = 'cadastros/form-excluir.html' 
    sucess_url = reverse_lazy('listar-ficha') 
    
   # def get_object(self, queryset=None):       
    #    self.object = get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)     
     #   return self.object 
    

class ExercicioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"  
    model = Exercicio  
    template_name = 'cadastros/form-excluir.html' 
    sucess_url = reverse_lazy('listar-exercicio') 
    
    #def get_object(self, queryset=None):       
     #   self.object = get_object_or_404(Cliente, pk=self.kwargs['pk'], usuario=self.request.user)     
      #  return self.object 
       
    
################################ LISTA ######################################       
     
    
class ClienteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario"   
    model = Cliente
    template_name = 'cadastros/listas/cliente.html' 
    
    #def get_queryset(self):
     #   self.object_list = Cliente.objects.filter(usuario=self.request.user)
      #  return self.object_list
 
class FuncionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"   
    model = Funcionario   
    template_name = 'cadastros/listas/funcionario.html' 
    
   # def get_queryset(self):
    #    self.object_list = Funcionario.objects.filter(usuario=self.request.user)
     #   return self.object_list
    
    
class FichaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"   
    model = Ficha  
    template_name = 'cadastros/listas/ficha.html'  
    
   # def get_queryset(self):
    #    self.object_list = Ficha.objects.filter(usuario=self.request.user)
     #   return self.object_list

class ExercicioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador",u"Funcionario",u"Cliente"   
    model = Exercicio  
    template_name = 'cadastros/listas/exercicio.html'
    
   # def get_queryset(self):
    #    self.object_list = Exercicio.objects.filter(usuario=self.request.user)
     #   return self.object_list
 
               
           
           
    


