from django.db import models


class PercursoAcademico(models.Model):
    nome = models.CharField(max_length=150)
    dataInicio = models.DateField(null=True, default=None)
    dataFim = models.DateField(null=True, default=None)
    instituicao = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=150)
    ano = models.CharField(max_length=4)
    semestre = models.CharField(max_length=4)
    disciplina = models.CharField(max_length=50)
    ects = models.CharField(max_length=2)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.disciplina


class OutrasCompetencias(models.Model):
    nome = models.CharField(max_length=150)
    dataInicio = models.DateField(null=True, default=None)
    dataFim = models.DateField(null=True, default=None)
    instituicao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + " : " + self.instituicao


class ProjectosDesenvolvidos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=3000)

    def __str__(self):
        return self.nome


class LaboratoriosRealizados(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class ExperienciaProfissional(models.Model):
    nome = models.CharField(max_length=150)
    dataInicio = models.DateField(null=True, default=None)
    dataFim = models.DateField(null=True, default=None)
    descricao = models.CharField(max_length=3000)

    def __str__(self):
        return self.nome


class Contacto(models.Model):
    tipo = models.CharField(max_length=150)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.tipo


class Autor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
