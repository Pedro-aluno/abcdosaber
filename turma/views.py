from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cadastro(request):
    return render(request, 'turma/cadastroTurma.html')

def lista(request):
    return render(request, 'turma/listarTurmas.html')

def ausencia(request):
    return render(request, 'turma/registroAusencia.html')