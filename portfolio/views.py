from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.


def home_page_view(request):
    if not request.user.is_authenticated:
        return redirect('portfolio:login')

    return render(request, 'portfolio/home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio:home')
        else:
            return render(request, "portfolio/login.html", {'message': "Invalid credentials."})
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return render(request, "portfolio/login.html", {"message": "Logged Out"})


def licenciatura_page_view(request):
    licenciatura1 = Licenciatura.objects.all().filter(ano='1Ano')
    licenciatura2 = Licenciatura.objects.all().filter(ano='2Ano')
    licenciatura3 = Licenciatura.objects.all().filter(ano='3Ano')

    context = {
        'licenciatura1': licenciatura1,
        'licenciatura2': licenciatura2,
        'licenciatura3': licenciatura3,
    }
    return render(request, 'portfolio/licenciatura.html', context)


def experiencia_profissional_page_view(request):
    experiencia_profissional = ExperienciaProfissional.objects.all()

    context = {
        'experiencia_profissional': experiencia_profissional
    }
    return render(request, 'portfolio/experiencia_profissional.html', context)


def contacto_page_view(request):
    contacto = Contacto.objects.all()

    return render(request, 'portfolio/contacto.html')


def outras_competencias_page_view(request):
    outras_competencias = OutrasCompetencias.objects.all()

    context = {
        'outras_competencias': outras_competencias
    }
    return render(request, 'portfolio/outras_competencias.html', context)


def percurso_academico_page_view(request):
    percurso_academico = PercursoAcademico.objects.all()

    context = {
        'percurso_academico': percurso_academico
    }
    return render(request, 'portfolio/percurso_academico.html', context)


def projectos_desenvolvidos_page_view(request):
    projectos_desenvolvidos = ProjectosDesenvolvidos.objects.all()

    context = {
        'projectos_desenvolvidos': projectos_desenvolvidos
    }
    return render(request, 'portfolio/projectos_desenvolvidos.html', context)


def experimente_voce_page_view(request):
    return render(request, 'portfolio/experimente_voce.html')


@login_required
def actualizacaoInfo_page_view(request):
    percursoAcademico = PercursoAcademicoForm()
    outrasCompetencias = OutrasCompetenciasForm()
    experienciaProfissional = ExperienciaProfissionalForm()
    licenciatura = LicenciaturaForm()

    dadosPercursoAcademico = PercursoAcademico.objects.all()
    dadosOutrasCompetencias = OutrasCompetencias.objects.all()
    dadosExperienciaProfissional = ExperienciaProfissional.objects.all()
    dadosLicenciatura = Licenciatura.objects.all()

    context = {
        'percursoAcademico': percursoAcademico,
        'outrasCompetencias': outrasCompetencias,
        'experienciaProfissional': experienciaProfissional,
        'licenciatura': licenciatura,
        'dadosPercursoAcademico': dadosPercursoAcademico,
        'dadosOutrasCompetencias': dadosOutrasCompetencias,
        'dadosExperienciaProfissional': dadosExperienciaProfissional,
        'dadosLicenciatura': dadosLicenciatura
    }

    return render(request, 'portfolio/adicionar_info.html', context)


def adicionar_info_page_view(request, prefix):
    if request.method == 'POST':
        if prefix == 'percursoAcademico':
            form = PercursoAcademicoForm(request.POST)
        elif prefix == 'outrasCompetencias':
            form = OutrasCompetenciasForm(request.POST)
        elif prefix == 'experienciaProfissional':
            form = ExperienciaProfissionalForm(request.POST)
        elif prefix == 'licenciatura':
            form = LicenciaturaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('portfolio:adicionar_info')
        else:
            return redirect('portfolio:adicionar_info')


def editar_info_page_view(request, prefix, item_id):
    if prefix == 'percursoAcademico':
        form = PercursoAcademicoForm(request.POST or None, instance=PercursoAcademico.objects.get(id=item_id))
    elif prefix == 'outrasCompetencias':
        form = OutrasCompetenciasForm(request.POST or None, instance=OutrasCompetencias.objects.get(id=item_id))
    elif prefix == 'experienciaProfissional':
        form = ExperienciaProfissionalForm(request.POST or None, instance=ExperienciaProfissional.objects.get(id=item_id))
    elif prefix == 'licenciatura':
        form = LicenciaturaForm(request.POST or None, instance=Licenciatura.objects.get(id=item_id))

    if form.is_valid():
        form.save()
        return redirect('portfolio:adicionar_info')

    context = {'form': form, 'prefix': prefix, 'item_id': item_id}
    return render(request, 'portfolio/editar_info.html', context)


def apagar_info_page_view(request, prefix, item_id):
    if prefix == 'percursoAcademico':
        PercursoAcademico.objects.get(id=item_id).delete()
    elif prefix == 'outrasCompetencias':
        OutrasCompetencias.objects.get(id=item_id).delete()
    elif prefix == 'experienciaProfissional':
        ExperienciaProfissional.objects.get(id=item_id).delete()
    elif prefix == 'licenciatura':
        Licenciatura.objects.get(id=item_id).delete()

    return redirect('portfolio:adicionar_info')
