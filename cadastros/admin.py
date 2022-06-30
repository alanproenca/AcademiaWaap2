from django.contrib import admin

# Importar as classes
from .models import  Cliente, Funcionario, Ficha, Exercicio

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Ficha)
admin.site.register(Exercicio)