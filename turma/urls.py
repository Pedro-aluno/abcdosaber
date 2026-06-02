from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path('cadastro/', views.cadastro , name='cadastro'),
    path('listar/', views.lista, name='listar'),
    path('registroAusencia/', views.ausencia, name='registro_ausencia'),    
    
]