
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.html import format_html

from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'        

class Pacote(models.Model):
    projeto = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=50)
    percent = models.IntegerField('Percentual', default=0)

    def __str__(self):
        return "{} | {}".format(self.projeto.name, self.name)

    class Meta:
        unique_together = (('projeto','name'),)

class Problem(models.Model):

    PROB_TYPE = (
        ('E', 'Erro'),
        ('Q', 'Dúvida'),
        ('S', 'Sugestão'),
        ('P', 'Pendência'),
    )

    PRIORITIES = (
        (0, 'Alta'),
        (1, 'Média'),
        (2, 'Baixa'),
    )

    pacote = models.ForeignKey( Pacote, on_delete=models.CASCADE, verbose_name='Pacote')
    title = models.CharField('Título', max_length=200)
    text = models.TextField('Descrição detalhada', blank=True)

    prob_type = models.CharField(
        'Tipo',
        max_length=1,
        choices=PROB_TYPE,
        default=' '
    )

    priority = models.IntegerField(
        'Prioridade',
        choices=PRIORITIES,
        default=1
    )

    versao = models.CharField('Versão', max_length=20, blank=True)

    complete = models.BooleanField('Concluído?', default=False)

    def colored_type(self):
        
        COLOR_TYPE = {
            'E': 'FF3333',
            'Q': '00AA00',
            'S': '00AA00',
            'P': '0000AA',
        }
        
        return format_html(
            '<span style="color: #{};">{}</span>',
            COLOR_TYPE[self.prob_type],
            self.get_prob_type_display(),
        )

    def __str__(self):
        return "{}".format(self.title)

    colored_type.short_description = 'Tipo'

    class Meta:
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'
        
    
class Note(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.TextField()