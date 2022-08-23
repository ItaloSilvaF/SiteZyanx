from django.db import models


class About(models.Model):

    nome_pagina = models.CharField(
        max_length=50, verbose_name='Página',  blank=False, null=False, default='About')
    titulo_pagina = models.CharField(
        max_length=50, verbose_name='Título',  blank=False, null=False, default=None)
    subtitulo_pagina = models.TextField(
        max_length=50, verbose_name='Subtítulo',  blank=True, null=True, default=None)
    titulo_descricao_pagina = models.CharField(
        max_length=500, verbose_name='Titulo da descrição', blank=False, null=True, default=None)
    descricao_pagina = models.TextField(
        max_length=500, verbose_name='Descrição', blank=False, null=True, default=None)
    publicado_pagina = models.BooleanField(
        verbose_name='Publicado', default=False)
    imagem_pagina = models.ImageField(
        upload_to='imagens_paginas/', blank=True, null=True, verbose_name='Background')

    def __str__(self):
        return self.nome_pagina