# Generated by Django 4.0.6 on 2022-08-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_home_descricao_quadrado_um_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='imagem_pagina',
            field=models.ImageField(default='', upload_to='imagens_paginas/', verbose_name='Background'),
        ),
    ]