from django.urls import path
from aplicaciones.blog import views


from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias_post, name='categorias_post'),
    path('categorias/<int:id>', views.ver_categoria, name='ver_categoria'),
    path('crear_post/', views.crear_post, name = 'crear_post'),
    path('registro/', views.registro, name = 'registro'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('acceder/', auth_views.LoginView.as_view(template_name='acceder.html'), name='acceder'),
    path('salir/', auth_views.LogoutView.as_view(template_name='salir.html'), name='salir'),
    path('<slug:slug>/', views.ver_post, name = 'ver_post'),
    path('<slug:slug>/coment/', views.agregar_comentario, name='agregar_comentario'),


    
]