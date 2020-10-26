# Generated by Django 3.1.2 on 2020-10-21 03:04

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201020_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('ini-cog', 'Engrenagem'), ('ini-users', 'Usuários'), ('ini-stats-up', 'Grafico'), ('ini-rocket', 'Foguete'), ('ini-mobile', 'Mobile'), ('ini-layers', 'Design')], max_length=12, verbose_name='Icone'),
        ),
    ]
