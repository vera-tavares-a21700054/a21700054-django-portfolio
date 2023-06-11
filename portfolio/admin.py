from django.contrib import admin
from .models import *

admin.site.site_title = 'Vera Tavares'
admin.site.site_header = 'Vera Tavares'

# Register your models here.

admin.site.register(Autor)
admin.site.register(PercursoAcademico)
admin.site.register(Licenciatura)
admin.site.register(OutrasCompetencias)
admin.site.register(ProjectosDesenvolvidos)
admin.site.register(LaboratoriosRealizados)
admin.site.register(ExperienciaProfissional)
admin.site.register(ExperimenteVoce)
admin.site.register(Contacto)
