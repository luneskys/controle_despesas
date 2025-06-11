from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_transacoes, name='listar_transacoes'),
    path('transacoes/nova/', views.criar_transacao, name='criar_transacao'),
    path('transacoes/editar/<int:id>/', views.editar_transacao, name='editar_transacao'),
    path('transacoes/excluir/<int:id>/', views.excluir_transacao, name='excluir_transacao'),
]
