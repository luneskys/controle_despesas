from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['categoria', 'valor', 'data', 'descricao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }