#  hello/urls.py

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('experiencia_profissional', views.experiencia_profissional_page_view, name='experiencia_profissional'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('outras_competencias', views.outras_competencias_page_view, name='outras_competencias'),
    path('percurso_academico', views.percurso_academico_page_view, name='percurso_academico'),
    path('projectos_desenvolvidos', views.projectos_desenvolvidos_page_view, name='projectos_desenvolvidos'),
    path('experimente_voce', views.experimente_voce_page_view, name='experimente_voce'),
    path('adicionar_info', views.actualizacaoInfo_page_view, name='adicionar_info'),
    path('apaga/<str:prefix>/<int:item_id>/', views.apagar_info_page_view, name='apaga'),
    path('edita/<str:prefix>/<int:item_id>/', views.editar_info_page_view, name='edita'),
    path('adiciona/<str:prefix>/', views.adicionar_info_page_view, name='adicionar'),
]
