# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Asistencia A Los Entrenamientos(models.Model):

    #__Asistencia A Los Entrenamientos_FIELDS__
    asistencia id = models.CharField(max_length=255, null=True, blank=True)
    id del atleta = models.CharField(max_length=255, null=True, blank=True)

    #__Asistencia A Los Entrenamientos_FIELDS__END

    class Meta:
        verbose_name        = _("Asistencia A Los Entrenamientos")
        verbose_name_plural = _("Asistencia A Los Entrenamientos")


class Entrenador(models.Model):

    #__Entrenador_FIELDS__
    id del entrenador = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    especialidad = models.CharField(max_length=255, null=True, blank=True)
    correo = models.CharField(max_length=255, null=True, blank=True)

    #__Entrenador_FIELDS__END

    class Meta:
        verbose_name        = _("Entrenador")
        verbose_name_plural = _("Entrenador")


class Programa De Entrenamiento(models.Model):

    #__Programa De Entrenamiento_FIELDS__
    id del programa = models.CharField(max_length=255, null=True, blank=True)
    nombre del programa = models.CharField(max_length=255, null=True, blank=True)
    descripción = models.CharField(max_length=255, null=True, blank=True)
    entrenador a cargo (nombre o id ) = models.CharField(max_length=255, null=True, blank=True)

    #__Programa De Entrenamiento_FIELDS__END

    class Meta:
        verbose_name        = _("Programa De Entrenamiento")
        verbose_name_plural = _("Programa De Entrenamiento")


class Registro De Competencias(models.Model):

    #__Registro De Competencias_FIELDS__
    id de registro  = models.CharField(max_length=255, null=True, blank=True)
    nombre del atleta = models.CharField(max_length=255, null=True, blank=True)
    id de atleta = models.CharField(max_length=255, null=True, blank=True)
    competencia (nombre del evento, liga, etc) = models.CharField(max_length=255, null=True, blank=True)
    nota:  = models.CharField(max_length=255, null=True, blank=True)
    info: = models.CharField(max_length=255, null=True, blank=True)

    #__Registro De Competencias_FIELDS__END

    class Meta:
        verbose_name        = _("Registro De Competencias")
        verbose_name_plural = _("Registro De Competencias")


class Atletas(models.Model):

    #__Atletas_FIELDS__
    nombre: = models.CharField(max_length=255, null=True, blank=True)
    apellido: = models.CharField(max_length=255, null=True, blank=True)
    sexo: = models.CharField(max_length=255, null=True, blank=True)
    genero (auto percepción): = models.CharField(max_length=255, null=True, blank=True)
    correo: = models.CharField(max_length=255, null=True, blank=True)
    afiliado: = models.CharField(max_length=255, null=True, blank=True)
    categoría: = models.CharField(max_length=255, null=True, blank=True)
    equipo: = models.CharField(max_length=255, null=True, blank=True)
    equipos a los que pertenece: = models.CharField(max_length=255, null=True, blank=True)
    país  = models.CharField(max_length=255, null=True, blank=True)
    nacionalidad = models.CharField(max_length=255, null=True, blank=True)
    madre, padre o tutor = models.CharField(max_length=255, null=True, blank=True)
    contacto (madre, padre o tutor) = models.CharField(max_length=255, null=True, blank=True)

    #__Atletas_FIELDS__END

    class Meta:
        verbose_name        = _("Atletas")
        verbose_name_plural = _("Atletas")



#__MODELS__END
