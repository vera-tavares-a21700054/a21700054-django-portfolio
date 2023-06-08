#  hello/urls.py

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('experiencia_profissional', views.experiencia_profissional_page_view, name='experiencia_profissional'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('outras_competencias', views.outras_competencias_page_view, name='outras_competencias'),
    path('percurso_academico', views.percurso_academico_page_view, name='percurso_academico'),
    path('projectos_desenvolvidos', views.projectos_desenvolvidos_page_view, name='projectos_desenvolvidos')
]