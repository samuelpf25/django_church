# Generated by Django 4.0.5 on 2022-06-19 19:19

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_informes_palavras_quemsomos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informes',
            name='chamada',
        ),
        migrations.RemoveField(
            model_name='informes',
            name='titulo',
        ),
        migrations.AddField(
            model_name='informes',
            name='tituloprimario',
            field=models.CharField(default=0, max_length=100, verbose_name='Título primário'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informes',
            name='titulosecundario',
            field=models.CharField(default=1, max_length=100, verbose_name='Título secundário'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='informes',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 750, 'width': 940}}, verbose_name='Imagem'),
        ),
    ]