from django.db import models

# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(
        primary_key=True,
        help_text="Número da turma",
        null=False,
)

    horarioAula = models.TimeField(
        null=False,
        help_text="Informe o horário da aula",
)

    duracaoAula = models.TimeField(
        null=False,
        help_text="Informe a duração da aula:"
)

    dataInicial = models.DateField(
        null=False,
        help_text="Informe a data de início da turma",
)

    dataFinal = models.DateField(
        null=False,
        help_text="Informe a data de término da turma",
)

    codigoTipoAtividade = models.CharField(
        max_length=70,
        null=False,
        help_text="Informe o código do tipo de atividade",
)

    matriculaMonitor = models.CharField(
        max_length=70,
        null=True,
        help_text="Informe a matrícula do monitor",
)

    idInsturor = models.CharField(
        null=False,
        max_length=70,
        help_text="Informe a matrícula do instrutor",
    )

    def __str__(self):
        return f"{self.numero} {self.horarioAula} {self.duracaoAula} {self.dataInicial} {self.dataFinal} {self.codigoTipoAtividade} {self.matriculaMonitor} {self.idInsturor}"