# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import UserForm
from django.contrib.auth.models import User

from django.shortcuts import render


# Create your views here.

def home(request):
    """
    la vue de base
    :param request: 
    :return: 
    """
    return render(request, "genius/home.html", {})


def contact(request):
    """
    page contact
    :param request: 
    :return: 
    """
    return render(request, "genius/contact.html", {})


def inteligence_artificiel(request):
    """
    la vue de competance
    :param request: 
    :return: 
    """
    return render(request, "genius/inteligence_artificiel.html", {})


def portefeuil(request):
    """
    la vue de portefeuil
    :param request: 
    :return: 
    """
    return render(request, "genius/portefeuil.html", {})


def presentation(request):
    """
    la vue de presentation
    :param request: 
    :return: 
    """
    return render(request, "genius/presentation.html", {})


def projet(request):
    """
    la vue de projet
    :param request: 
    :return: 
    """
    return render(request, "genius/projets.html", {})


def login(request):
    """
    la vue de login
    :param request: 
    :return: 
    """
    return render(request, "genius/login.html", {})


def dev_web(request):
    """
    la vue de developpement web
    :param request: 
    :return: 
    """
    return render(request, "genius/dev_web.html", {})


def dev_mobil(request):
    """
    la vue de developpement mobil
    :param request: 
    :return: 
    """
    return render(request, "genius/dev_mobil.html", {})


def automatisation(request):
    """
    la vue de automatisation des taches
    :param request: 
    :return: 
    """
    return render(request, "genius/automtisations.html", {})


def compteUser(request):
    """
    formulaire de l'utilisateur
    :param request:
    :return:
    """
    compte_user = User.objects.filter(id=1).only()
    return render(request, 'genius/projets.html', {'compte_user': compte_user})


def deconnexion(request):
    """
    déconnxion
    :param request:
    :return:
    """
    logout(request)
    return redirect('index')