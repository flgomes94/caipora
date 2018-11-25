from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import *
from leaflet.forms.widgets import LeafletWidget
# Create your views here.


class nova_denuncia(CreateView):
    model = Manifestacao
    form_class = ManifestacaoForm
    success_url = '/denuncia/'

class detalhe_manifestcao(DetailView,LeafletWidget):
    model = Manifestacao
    settings_overrides = {
            'DEFAULT_CENTER': (6.0, 45.0),
        }

    def get_context_data(self, **kwargs):
        print('teste')
        context = super().get_context_data(**kwargs)
        manifestacao = context['manifestacao']
        print (manifestacao.geom['coordinates'][0])
        return context



