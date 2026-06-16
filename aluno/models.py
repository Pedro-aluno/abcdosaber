from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(
        primary_key=True,
        help_text="Matrícula do aluno",
        
    )

    nome = models.CharField(
        max_length=70,
        null = False,
        help_text="Informe o nome do aluno",
    )
    
    data_inicial = models.DateField(
        null=False,
        help_text="Informe que horário o aluno começou a estudar",
    )

    data_final = models.DateField(
        help_text="Informe que horário o aluno terminou de estudar",
        null=True,
    )

    
    def __str__(self):
        return f"{self.matricula} {self.nome} {self.data_inicial} {self.data_final}"
