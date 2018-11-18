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

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('assunto','orgao'),
            Field('tipo','data'),
            Field('foto'),
            Field('geom'),
            Field('descricao'),
        )
        super(ManifestacaoForm, self).__init__(*args, **kwargs)

    #geom = PointField()
    class Meta:
        model = Manifestacao
        fields = ('assunto', 'orgao', 'tipo', 'data', 'foto', 'geom', 'descricao')
        widgets = {'geom': LeafletWidget}
