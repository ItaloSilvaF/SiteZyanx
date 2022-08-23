# Generated by Django 4.0.6 on 2022-08-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_home_descricao_pagina_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='descricao_quadrado_um',
        ),
        migrations.RemoveField(
            model_name='home',
            name='titulo_quadrado_um',
        ),
        migrations.AlterField(
            model_name='home',
            name='descricao_pagina',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='home',
            name='imagem_pagina',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_paginas/', verbose_name='Background'),
        ),
        migrations.AlterField(
            model_name='home',
            name='subtitulo_pagina',
            field=models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='home',
            name='titulo_pagina',
            field=models.CharField(default=None, max_length=50, verbose_name='Título'),
        ),
    ]