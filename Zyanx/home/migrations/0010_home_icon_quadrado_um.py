# Generated by Django 4.0.6 on 2022-08-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_home_descricao_quadrado_cinco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='icon_quadrado_um',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='icon_home/'),
        ),
    ]