from django.db import models
from stdimage import StdImageField
import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualizaçao', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    class Meta:
        abstract=True

class Eventos(Base):
    titulo = models.CharField('Título', max_length=100)
    chamada = models.TextField('Chamada', max_length=200)
    descricao = models.TextField('Descrição', max_length=2000)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations = {'thumb': {'width': 360, 'height': 293.33, 'crop': True}})
    data = models.DateTimeField('Data')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __int__(self):
        return self.titulo

class Palavras(Base):
    titulo = models.CharField('Título', max_length=100)
    chamada = models.TextField('Chamada', max_length=200)
    descricao = models.TextField('Descrição', max_length=2000)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations = {'thumb': {'width': 360, 'height': 293.33, 'crop': True}})
    data = models.DateTimeField('Data')

    class Meta:
        verbose_name = 'Palavra'
        verbose_name_plural = 'Palavras'

    def __int__(self):
        return self.titulo

class Informes(Base):
    tituloprimario = models.CharField('Título primário', max_length=100)
    titulosecundario= models.CharField('Título secundário', max_length=100)
    descricao = models.TextField('Descrição', max_length=2000)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations = {'thumb': {'width': 940, 'height': 750, 'crop': True}})
    data = models.DateTimeField('Data')

    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'

    def __int__(self):
        return self.titulo

class QuemSomos(Base):
    titulo = models.CharField('Título da descrição', max_length=100)
    descricao = models.TextField('Descrição', max_length=400)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations = {'thumb': {'width': 455, 'height': 289.89, 'crop': True}})

    class Meta:
        verbose_name = 'Quem Somos'
        verbose_name_plural = 'Quem Somos'

    def __int__(self):
        return self.titulo