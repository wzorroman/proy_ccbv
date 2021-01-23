from django.contrib import admin

from .models import Encuesta, Pregunta, Respuesta


class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion',
                    'format_creado', 'format_actualizado')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('actualizado',)

    def format_creado(self, obj):
        return obj.creado.strftime("%d/%m/%Y %H:%M:%S") if obj.creado else '-'
    
    def format_actualizado(self, obj):
        return obj.actualizado.strftime("%d/%m/%Y %H:%M:%S") if obj.actualizado else '-'

    format_creado.short_description = 'Creado'
    format_creado.admin_order_field = 'creado'
    format_actualizado.short_description = 'Actualizado'
    format_actualizado.admin_order_field = 'actualizado'


class PreguntaAdmin(admin.ModelAdmin):
    list_display=('id', 'encuesta', 'pregunta', 'pregunta_previa', 'pregunta_sgte', 
                  'format_creado', 'format_actualizado')
    search_fields = ('id', 'pregunta')
    list_filter = ('actualizado',)

    def format_creado(self, obj):
        return obj.creado.strftime("%d/%m/%Y %H:%M:%S") if obj.creado else '-'
    
    def format_actualizado(self, obj):
        return obj.actualizado.strftime("%d/%m/%Y %H:%M:%S") if obj.actualizado else '-'

    format_creado.short_description = 'Creado'
    format_creado.admin_order_field = 'creado'
    format_actualizado.short_description = 'Actualizado'
    format_actualizado.admin_order_field = 'actualizado'


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'pregunta', 'respuesta', 'format_creado', 
                    'format_actualizado')
    search_fields = ('id', 'pregunta')
    list_filter = ('actualizado',)

    def format_creado(self, obj):
        return obj.creado.strftime("%d/%m/%Y %H:%M:%S") if obj.creado else '-'

    def format_actualizado(self, obj):
        return obj.actualizado.strftime("%d/%m/%Y %H:%M:%S") if obj.actualizado else '-'

    format_creado.short_description = 'Creado'
    format_creado.admin_order_field = 'creado'
    format_actualizado.short_description = 'Actualizado'
    format_actualizado.admin_order_field = 'actualizado'


admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
