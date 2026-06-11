from django.db import models

from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    id = models.AutoField(
        null= False,
        primary_key= True,
        help_text= "Informe o id do instrutor"
    )
    
    rg = models.CharField(
        max_length= 10,
        null= False,
        help_text="Informe o rg do instrutor"
    )
    
    nome = models.CharField(
        max_length= 70,
        null= False,
        help_text="Informe o nome do instrutor"
    )
    
    dataNascimento = models.DateField(
        null= False,
        help_text="Informe a data de nascimento do instrutor"
    )
    
    telefone = models.CharField(
        max_length= 9,
        null= False,
        help_text="Informe o número do instrutor"
    )
    
    ddd = models.CharField(
        max_length= 3,
        null= True,
        help_text= "Informe o ddd"
    )
 

    codigoTitulo = models.ForeignKey(
        Titulo,
        null= True,
        blank=True,
        related_name='titulo',
        on_delete= models.SET_NULL,
        db_column='codigoTitulo',
        help_text= "Informe o codigo do Titulo"
    )
    
    def __str__(self):
        return f"{self.id} {self.rg} {self.nome} {self.dataNascimento} {self.telefone} {self.ddd} {self.codigoTitulo}"
