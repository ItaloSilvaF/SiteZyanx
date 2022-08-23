from distutils.command.upload import upload
from email.policy import default
from django.db import models


class Home(models.Model):

    nome_pagina = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='Home')
    titulo_pagina = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    subtitulo_pagina = models.TextField(
        max_length=50, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    descricao_pagina = models.TextField(
        max_length=500, verbose_name='Descrição', blank=True, null=True, default=None)
    publicado_pagina = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_pagina = models.ImageField(
        upload_to='imagens_paginas/', blank=True, null=True, verbose_name='Background')
    titulo_quadrado_um = models.CharField(
        max_length=50, verbose_name='Título do quadrado 1', blank=True, null=True, default=None)
    descricao_quadrado_um = models.TextField(
        max_length=500, verbose_name='Descrição do quadrado 1', blank=True, null=True, default=None)
    titulo_quadrado_dois = models.CharField(
        max_length=50, verbose_name='Título do quadrado 2', blank=True, null=True, default=None)
    descricao_quadrado_dois = models.TextField(
        max_length=500, verbose_name='Descrição do quadrado 2', blank=True, null=True, default=None)
    titulo_quadrado_tres = models.CharField(
        max_length=50, verbose_name='Título do quadrado 3', blank=True, null=True, default=None)
    descricao_quadrado_tres = models.TextField(
        max_length=500, verbose_name='Descrição do quadrado 3', blank=True, null=True, default=None)
    titulo_quadrado_quatro = models.CharField(
        max_length=50, verbose_name='Título do quadrado 4', blank=True, null=True, default=None)
    descricao_quadrado_quatro = models.TextField(
        max_length=500, verbose_name='Descrição do quadrado 4', blank=True, null=True, default=None)
    titulo_quadrado_cinco = models.CharField(
        max_length=50, verbose_name='Título do quadrado 5', blank=True, null=True, default=None)
    descricao_quadrado_cinco = models.TextField(
        max_length=500, verbose_name='Descrição do quadrado 5', blank=True, null=True, default=None)

    def __str__(self):
        return self.nome_pagina
