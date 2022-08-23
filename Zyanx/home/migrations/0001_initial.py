# Generated by Django 4.1 on 2022-08-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pagina', models.CharField(default='Home', max_length=50, verbose_name='Página')),
                ('titulo_pagina', models.CharField(default=None, max_length=50, verbose_name='Título')),
                ('subtitulo_pagina', models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='Subtítulo')),
                ('descricao_pagina', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Descrição')),
                ('publicado_pagina', models.BooleanField(default=False, verbose_name='Publicado')),
                ('imagem_pagina', models.ImageField(blank=True, null=True, upload_to='imagens_paginas/', verbose_name='Background')),
            ],
        ),
    ]
