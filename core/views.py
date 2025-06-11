from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transacao
from .forms import TransacaoForm

@login_required
def listar_transacoes(request):
    transacoes = Transacao.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'core/lista_transacoes.html', {'transacoes': transacoes})

@login_required
def criar_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.usuario = request.user
            transacao.save()
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm()
    return render(request, 'core/nova_transacao.html', {'form': form})

@login_required
def editar_transacao(request, id):
    transacao = get_object_or_404(Transacao, id=id, usuario=request.user)
    if request.method == 'POST':
        form = TransacaoForm(request.POST, instance=transacao)
        if form.is_valid():
            form.save()
            return redirect('listar_transacoes')
    else:
        form = TransacaoForm(instance=transacao)
    return render(request, 'core/editar_transacao.html', {'form': form})

@login_required
def excluir_transacao(request, id):
    transacao = get_object_or_404(Transacao, id=id, usuario=request.user)
    if request.method == 'POST':
        transacao.delete()
        return redirect('listar_transacoes')
    return render(request, 'core/confirmar_exclusao.html', {'transacao': transacao})
