# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Problem, Project, Pacote

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'pacote', 'colored_type', 'priority', 'complete' )
    list_filter = ('pacote__projeto', 'prob_type', 'priority','complete')
    search_fields = ('title',)
    ordering = ['complete', 'priority']

@admin.register(Pacote)
class PacoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'projeto', 'percent')
    list_filter = ('projeto',)
    fields = ('name', 'projeto', 'percent')
    search_fields = ('name',)

class PacoteInline(admin.TabularInline):
    model = Pacote
    extra = 1    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('get_percent',)
    list_display = ('name', 'get_percent')
    inlines = [
        PacoteInline,
    ]

    def get_percent(self, obj):
        """
        Calcula a média percentual do projeto
        """
        pacotes = Pacote.objects.filter(projeto=obj)
        if len(pacotes) > 0:
            soma = 0
            for pacote in pacotes:
                soma += pacote.percent

            return int(soma/len(pacotes)) 
        else:
            return 0

    get_percent.short_description = 'Percentual (%)'

