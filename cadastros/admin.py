from django.contrib import admin
from cadastros.models import Modulo
from cadastros.models import Modalidade
from cadastros.models import Programa
from cadastros.models import Analista
from cadastros.models import Alteracao
from cadastros.models import Arquivo
# Register your models here.

# class para edicao dos campos de  formulario exibidos na tela
class ProgramaAdmin(admin.ModelAdmin):
        list_display = ('modulo','modalidade','programa','descricao',)
        search_fields = ('programa','descricao',)
        list_filter = ('modulo','modalidade','programa','descricao',)
        ordering = ('programa',)
        filter_horizontal = ('arquivos',)
        fieldsets = [
        (None, {'fields': ['modulo',
                           'modalidade', 'programa',
                           ('descricao', 'arquivos'), ]}),
        ]
	fieldsets = [
		('Modulo',      {'fields': [('modulo','modalidade')]}),
		('Programa',      {'fields': ['programa','descricao']}),
		('Arquivos',      {'fields': ['arquivos']}),
	]
 
          


admin.site.register(Modulo)
admin.site.register(Modalidade)
admin.site.register(Programa,ProgramaAdmin)
admin.site.register(Analista)
admin.site.register(Alteracao)
admin.site.register(Arquivo)



