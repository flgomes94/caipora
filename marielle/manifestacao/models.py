from django.db import models
from djgeojson.fields import *

# Create your models here.

TIPOS = [
    ('1', 'Denúncia'),
    ('2', 'Reclamação'),
    ('3', 'Solicitação'),
    ('4', 'Sugestão'),
]

class Manifestacao(models.Model):
    assunto = models.CharField(max_length=250)
    orgao = models.CharField(max_length=250)
    tipo = models.CharField(max_length=1,choices=TIPOS,default='1')
    data = models.DateTimeField()
    visibilidade = models.BooleanField(default=True)
    highlights = models.IntegerField(default=0)
    foto = models.ImageField(blank=True, null=True)
    descricao = models.TextField()
    geom = PointField()

    def __unicode__(self):
        return self.assunto
    @property
    def picture_url(self):
        return self.foto.url

