from django import forms
from django.forms import ModelForm
from .models import *


class PercursoAcademicoForm(forms.ModelForm):
    class Meta:
        model = PercursoAcademico
        fields = '__all__'


class OutrasCompetenciasForm(forms.ModelForm):
    class Meta:
        model = OutrasCompetencias
        fields = '__all__'


class ExperienciaProfissionalForm(forms.ModelForm):
    class Meta:
        model = ExperienciaProfissional
        fields = '__all__'


class LicenciaturaForm(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = '__all__'
