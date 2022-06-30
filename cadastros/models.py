from tabnanny import verbose
from django.db import models
#from django.contrib.auth.models import User


#def user_auth(instance, filename):
 #   return "usuario_{0}/{1}".format(instance.user.id, filename)

# Create your models here.
    
class  Cliente(models.Model):
    cpf = models.IntegerField(verbose_name = "CPF:", unique=True)
    nome = models.CharField(max_length=255, verbose_name="Nome:")
    #matricula = models.IntegerField(verbose_name="Matricula")
    email= models.EmailField(max_length=150, verbose_name="Email:",blank=True,null=True)
    dtnascimento = models.DateField(verbose_name="Data Nascimento:",max_length=10, help_text="DD/MM/AAAA")     
    opcoes = ( ('Masculino', ('Masculino')), ('Feminino', ('Feminino')),('Não Definido',('Não Definido')))   
    sexo = models.CharField(max_length=50,verbose_name="Sexo:", choices=opcoes)        
    endereco = models.CharField(max_length=150,verbose_name="Endereço:")
    numero = models.IntegerField(verbose_name="Número:")
    complemento = models.CharField(max_length=30, verbose_name="Complemento:",blank=True,null=True)
    bairro = models.CharField(max_length=50, verbose_name="Bairro:")
    cep = models.IntegerField(verbose_name="CEP:")
    telefone = models.IntegerField(verbose_name="Telefone:",blank=True,null=True)
    celular = models.IntegerField(verbose_name="Celular:", blank=True,null=True) 
   # usuario =  models.ForeignKey(User, on_delete=models.PROTECT)    
    
    def __str__(self):
        return "{} ({})".format(self.cpf, self.nome, self.email, self.dtnascimento, self.sexo, self.endereco, self.numero , self.complemento, self.bairro, self.cep, self.telefone, self.celular) 
  
class  Funcionario(models.Model):
    matricula = models.IntegerField(verbose_name = "Matricula:", default="", unique=True)
    cpf = models.IntegerField(verbose_name = "CPF:",default="", unique=True)
    nome = models.CharField(max_length=255, verbose_name="Nome:")
    #matricula = models.IntegerField(verbose_name="Matricula")
    email= models.EmailField(max_length=150, verbose_name="Email:",blank=True,null=True)
    dtnascimento = models.DateField(verbose_name="Data Nascimento:", help_text="DD/MM/AAAA")    
    opcoes = ( ('Masculino', ('Masculino')), ('Feminino', ('Feminino')),('Não Definido',('Não Definido')))   
    sexo = models.CharField(max_length=50,verbose_name="Sexo:", choices=opcoes)        
    endereco = models.CharField(max_length=150, verbose_name="Endereço:")
    numero = models.IntegerField(verbose_name="Número:")
    complemento = models.CharField(max_length=30, verbose_name="Complemento:",blank=True,null=True)
    bairro = models.CharField(max_length=50, verbose_name="Bairro:")
    cep = models.IntegerField(verbose_name="CEP:")
    telefone = models.IntegerField(verbose_name="Telefone:",blank=True,null=True)
    celular = models.IntegerField(verbose_name="Celular:",blank=True,null=True)  
    dtadmissao =models.DateField(verbose_name="Data Admissão:", help_text="DD/MM/AAAA")  
    dtdemissao =models.DateField(verbose_name="Data Demissao:", help_text="DD/MM/AAAA",blank=True,null=True)
      
    def __str__(self):
         return "{} ({})".format(self.matricula, self.cpf, self.nome, self.email, self.dtnascimento, self.sexo, self.endereco, self.numero, self.complemento, self.bairro, self.cep, self.telefone, self.celular, self.dtadmissao, self.dtdemissao)  
   
       
class  Exercicio(models.Model):
    repeticao =  models.IntegerField(verbose_name = "Repetições:")
    nome = models.CharField(max_length=255,verbose_name = "Nome do Exercicio:")
    tipoTreino = models.CharField(max_length=255,verbose_name = "Tipo de Treino:")
    descricao = models.TextField(max_length=500,verbose_name = "Descrição:")
    arquivo = models.FileField(upload_to="gif/")
  # imagem = models.ImageField(null=True, blank=True, upload_to="i")
    #usuario = models.ForeignKey(User, on_delete=models.PROTECT) 
        
    def __str__(self):
         return "{} ({})".format(self.repeticao, self.nome, self.tipoTreino, self.descricao)  
     
     
class  Ficha(models.Model):
    nome = models.CharField(max_length=100,verbose_name = "Nome da Ficha:")
    #cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT,verbose_name = "Cliente:") 
    #funcionario =models.CharField(Funcionario, on_delete=models.PROTECT)
    cliente = models.CharField(max_length=100,verbose_name = "Cliente:") 
   # cliente = models.ManyToManyField(Cliente)
    funcionario = models.CharField(max_length=100,verbose_name = "Funcionário:")
    exercicio = models.CharField(max_length=100,verbose_name = "Exercicio:")
    arquivo = models.FileField(upload_to="gif/")
   # exercicio = models.ManyToManyField(Exercicio)
   # imagem = models.ImageField()
   # usuario = models.ForeignKey(User, on_delete=models.PROTECT) 
 
    def __str__(self):
         return "{} ({})".format(self.nome, self.cliente, self.funcionario, self.exercicio)   
     
     
  
     

     
           
              
              
                            
     

     

         
     


     

  


         

