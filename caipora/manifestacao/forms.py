from django.forms import ModelForm
from django import forms
from .models import Manifestacao
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget
from django.contrib.admin import widgets
from crispy_forms.bootstrap import InlineField

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div, Field
from crispy_forms.layout import Layout
from crispy_forms import bootstrap, layout

'''
class ManifestacaoForm(ModelForm):
    geom = PointField()
    #data = forms.DateTimeField()
    class Meta:
        model = Manifestacao
        fields = ('assunto', 'orgao','tipo','data','foto', 'geom', 'descricao')

    def __init__(self,*args,**kwargs):
        super(ManifestacaoForm,self).__init__(*args,**kwargs)
        self.fields['data'].widget= widgets.AdminDateWidget()

'''

class ManifestacaoForm(ModelForm):
    class Meta:
        model = Manifestacao
        fields = ('assunto', 'orgao', 'tipo', 'data', 'foto', 'geom', 'descricao')
        widgets = {'geom': LeafletWidget}
        labels = {
            'data':'Data de ocorrência',
            'geom':'Escolha a localidade exata da sua Manifestação',
            'assunto':'Título da Manifestação',
            'orgao': 'Instituição destinatária da Manifestação',
            'tipo':'Tipo',
            'foto': 'Foto',
            'descricao': 'Descreva sua Manifestação',
        }
        help_texts = {
            'data': 'Caso não saiba um horário exato, ofereça uma estimativa de horário do ocorrido ou '
                    'de percebido o problema em questão',
            'assunto':'(Escolha um título para sua manifestação. Quanto mais direto, mais fácil '
                      'será para mobilizar sua causa.'
                      ' Ex:UPA sem geldadeira!)',
            'orgao': 'Sua Manifestação tem um órgão responsável. Pode ser importante apontar uma'
                     ' organização ao qual considere que seja a recomendada para tentar solucionar o seu problema.'
                     '\nEx: Prefeitura de Salvador',
            'tipo': 'Selecione o tipo que mais se adeque a sua manifestação',
            'foto': 'Você deve tomar cuidados com sua foto. Esta deve ilustrar exatamente o seu problema '
                    'consulte nosso manual para saber as regras que adotamos para não ter uma manifestação retirada.',
            'descricao': 'Descreva sua Manifestação. É a hora de por a boca no trombone!',

        }


'''
class ManifestacaoForm(ModelForm):
    geom = PointField()
    #data = forms.DateTimeField()
    class Meta:
        model = Manifestacao
        fields = ('assunto', 'orgao','tipo','data','foto', 'geom', 'descricao')

    def __init__(self,*args,**kwargs):
        super(ManifestacaoForm,self).__init__(*args,**kwargs)
        self.fields['data'].widget= widgets.AdminDateWidget()
'''