from django.db.models import query
from django.http import request
from django.http.response import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from .forms import PostForm, UsuarioForm, UsuarioActualizarForm, ComentariosForm
from .models import Categorias, Comentarios, Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def inicio(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts1 = posts.filter(titulo__icontains = queryset)
        posts2 = posts.filter(descripcion__icontains = queryset)
        posts3 = posts.filter(autor__username__icontains = queryset)
        posts = posts1.union(posts2).union(posts3)
    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    template = 'index.html'
    contexto = {
        'posts':posts
    }
    return render(request, template, contexto)

def categorias_post(request):
    queryset = request.GET.get("buscar")
    categorias = Categorias.objects.filter(estado = True)
    if queryset:
        categorias = Categorias.objects.filter(nombre__icontains = queryset)
    paginator = Paginator(categorias,4)
    page = request.GET.get('page')
    categorias = paginator.get_page(page)
    template = 'categorias_post.html'
    contexto = {
        'categorias':categorias,
    }
    return render(request, template, contexto)

def ver_categoria(request, id):
    cat = Categorias.objects.get(pk=id)
    posts = Post.objects.filter(estado = True, categoria = id)
    template = 'ver_categoria.html'
    contexto = {
        'categoria': cat,
        'posts':posts,
    }
    return render(request, template, contexto)

def ver_post(request, slug):
    post = Post.objects.get(slug = slug)
    template = 'post.html'
    contexto = {
        'post':post
    }
    return render(request, template, contexto)

def crear_post(request):
    if not request.user.is_authenticated:
        return redirect('blog:acceder')
    if not request.user.groups.filter(name='escritor').exists():
        if not request.user.is_superuser:
            return redirect('blog:acceder')
    formulario = PostForm(request.POST or None)
    if request.method == "POST":
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog:ver_post', post.slug)
    template = 'crear_post.html'
    contexto = {
        'formulario':formulario
    }
    return render(request, template, contexto)

def editar_post(request):
    if not request.user.is_authenticated:
        return redirect('blog:acceder')
    formulario = PostForm(request.POST or None)
    if request.method == "POST":
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog:ver_post', post.slug)
    template = 'crear_post.html'
    contexto = {
        'formulario':formulario
    }
    return render(request, template, contexto)

def registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST or None)
        if formulario.is_valid():
            usuario = formulario.save()
            messages.success(request, 'Cuenta creada')
            return redirect('blog:acceder')
    else:
        formulario = UsuarioForm()
    template = 'registro.html'
    contexto = {
        'formulario':formulario,
    }
    return render(request, template, contexto)

@login_required    
def perfil(request):
    if request.method == 'POST':
        u_form = UsuarioActualizarForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Su cuenta se actualizo correctamente')
            return redirect('blog:inicio')
    else:
        u_form = UsuarioActualizarForm(instance=request.user)
    template = 'perfil.html'
    contexto = {
        'u_form':u_form,
    }
    return render(request, template, contexto)

def agregar_comentario(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = ComentariosForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.post = post
            comentario.save()
            return redirect('blog:ver_post', post.slug)
    else:
        form = ComentariosForm()
    template = 'agregar_comentario.html'
    contexto = {
        'post':post,
        'form':form,
    }
    return render(request, template, contexto)


