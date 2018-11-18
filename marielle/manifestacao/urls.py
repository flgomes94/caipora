from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.urls import path
from . import views
from .models import Manifestacao

urlpatterns = [
    path('map/', TemplateView.as_view(template_name='manifestacao/mapa.html'), name='home'),
    path('data.geojson', GeoJSONLayerView.as_view(model=Manifestacao, properties=('assunto', 'descricao', 'picture_url')), name='data'),
    path('denuncia/nova', views.nova_denuncia,name='nova_denuncia'),
    path('', TemplateView.as_view(template_name='base/base.html')),
]