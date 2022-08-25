from django.db import models


class About(models.Model):

    nome_pagina = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_pagina = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    subtitulo_pagina = models.TextField(
        max_length=50, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    titulo_descricao_pagina = models.CharField(
        max_length=50, verbose_name='Titulo da descrição', blank=False, null=True, default=None)
    descricao_pagina = models.TextField(
        max_length=500, verbose_name='Descrição', blank=False, null=True, default=None)
    publicado_pagina = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_pagina = models.ImageField(
        upload_to='imagens_about/imagens_background', blank=True, null=True, verbose_name='Background')
    titulo_texto_um = models.CharField(
        max_length=50, verbose_name='Titulo texto 1', blank=True, null=True, default=None)
    texto_um = models.TextField(
        max_length=500, verbose_name='Texto 1', blank=True, null=True, default=None)
    imagem_texto_um = models.ImageField(
        upload_to='imagens_about/imagens_texto_um', blank=True, null=True, verbose_name='Imagem do texto 1')
    titulo_texto_dois = models.CharField(
        max_length=50, verbose_name='Titulo texto 2', blank=True, null=True, default=None)
    texto_dois = models.TextField(
        max_length=500, verbose_name='Texto 2', blank=True, null=True, default=None)
    imagem_texto_dois = models.ImageField(
        upload_to='imagens_about/imagens_texto_dois', blank=True, null=True, verbose_name='Imagem do texto 2')
    titulo_texto_tres = models.CharField(
        max_length=50, verbose_name='Titulo texto 3', blank=True, null=True, default=None)
    texto_tres = models.TextField(
        max_length=500, verbose_name='Texto 3', blank=True, null=True, default=None)
    imagem_texto_tres = models.ImageField(
        upload_to='imagens_about/imagens_texte_tres', blank=True, null=True, verbose_name='Imagem do texto 3')

    def __str__(self):
        return self.nome_pagina
