from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    username = models.CharField(max_length= 100, null=True)
    email = models.CharField(max_length= 200, null=True)
    password = models.CharField(max_length= 15, null=True)
    password1 = models.CharField(max_length= 15, null=True)
    
def __str__(self):
    return "{} ({})".format(self.username, self.email, self.password, self.password1) 
      
