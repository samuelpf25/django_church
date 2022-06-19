from django.contrib import admin

from .models import Eventos, Palavras, Informes, QuemSomos

@admin.register(Eventos)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')

@admin.register(Palavras)
class PalavrasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')

@admin.register(Informes)
class InformesAdmin(admin.ModelAdmin):
    list_display = ('tituloprimario', 'data')

@admin.register(QuemSomos)
class QuemSomosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
