from django import forms
from django.forms import ModelForm
from .models import Tarefa


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa  # especifica a classe de models.py à qual este formulário está associado

        # fields permite especificar os campos da classe que queremos que apareçam no formulário.
        #   - '__all__' apresenta todos.
        #   - podemos ter um subset: fields = ['titulo', 'prioridade']
        # alternativamente, pode-se usar a variável exclude para especificar os campos que se pretendem excluir do formulário
        fields = '__all__'

        # Para um conjunto de propriedade da classe (titulo, prioridade, concluido, etc),
        # o dicionário widgets permite configurar o elemento HTML input correspondente,
        # através de um dicionario de atributos de formatação (especificação de classes, placeholder, propriedades, etc).
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        # o dicionário labels especifica o texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }

        # o dicionário help_texts contém, para um atributo, um texto auxiliar a apresentar por baixo da janela de inserção
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }