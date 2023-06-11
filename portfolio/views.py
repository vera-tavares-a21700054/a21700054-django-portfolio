from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
