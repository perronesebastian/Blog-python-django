from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField('Nombre de la categoria', max_length=100, null=False, blank=False)
    imagen = models.URLField(max_length=255, null=True, blank=True)
    estado = models.BooleanField('Categoria activada/Categoria no activada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    escritor = models.BooleanField('Es escritor/No es escritor', default = False)

    def __str__(self):
        return f'{self.user.username}'


class Post(models.Model):
    titulo = models.CharField('Titulo del post', max_length=90, null=False, blank=False)
    slug = models.CharField('Slug', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripcion', max_length=110, null=True, blank=True)
    contenido = RichTextField()
    imagen = models.URLField(max_length=1000, null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificacion', auto_now=True)

    def __str__(self):
        return self.texto


