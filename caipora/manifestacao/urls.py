from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .models import Manifestacao

urlpatterns = [
    path('denuncia/', TemplateView.as_view(template_name='manifestacao/mapa.html'), name='home'),
    path('denuncia/nova', views.nova_denuncia.as_view(),name='nova_denuncia'),
    path('denuncia/<int:pk>/',views.detalhe_manifestcao.as_view(), name='manifestacao'),
    path('data.geojson', GeoJSONLayerView.as_view(model=Manifestacao, properties=('assunto', 'descricao', 'picture_url')), name='data'),
    path('', TemplateView.as_view(template_name='base/base.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)