from django.db import models
from django.conf import settings

class Categoria(models.Model):
    TIPO_CHOICES = (
        ('despesa', 'Despesa'),
        ('receita', 'Receita'),
    )
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.categoria.nome} - R${self.valor}'
