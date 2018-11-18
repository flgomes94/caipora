from django.shortcuts import render,redirect
from .forms import *

# Create your views here.


def nova_denuncia(request):
    form = ManifestacaoForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        form = ManifestacaoForm(request.POST, request.FILES)
        if form.is_valid():
            manifestacao = form.save(commit=False)
            manifestacao.save()
            return redirect('home')

    else:
        form = ManifestacaoForm()
    return render(request, 'manifestacao/nova_denuncia.html',{'form':form})
'''
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'nova_denuncia.html', {'form': form})
'''
