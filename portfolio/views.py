from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def home_page_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

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
            return redirect('home')
        else:
            return render(request, "portfolio/login.html", {'message': "Invalid credentials."})
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return render(request, "portfolio/login.html")


@login_required
def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')



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
    return render(request, 'portfolio/outras_competencias.html')


def percurso_academico_page_view(request):
    return render(request, 'portfolio/percurso_academico.html')


def projectos_desenvolvidos_page_view(request):
    return render(request, 'portfolio/projectos_desenvolvidos.html')
