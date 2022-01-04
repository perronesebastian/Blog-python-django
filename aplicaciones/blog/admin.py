from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categorias

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Perfil

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['user', 'email']
    list_display = ('user',)
    resource_class = AutorResource

admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Post)
admin.site.register(Perfil)
admin.site.register(Comentarios)