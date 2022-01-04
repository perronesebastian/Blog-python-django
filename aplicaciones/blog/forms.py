from django import forms
from django.db.models import fields
from django.views.generic.edit import CreateView
from .models import Categorias, Post, Perfil, Comentarios
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['estado', 'autor']

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name', 'password1', 'password2']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ['user', 'escritor']

class UsuarioActualizarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name']

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('texto',)




