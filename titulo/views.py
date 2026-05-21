from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_view(request):
    return HttpResponse('<p>Minha View do App Títulos</p>')

def show_oi(request):
    return HttpResponse('<p>Ola</p>')
