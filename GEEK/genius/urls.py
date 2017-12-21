# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accueil/artificiel/$', views.inteligence_artificiel, name='inteligence_artificiel'),
    url(r'^accueil/dev_web/$', views.dev_web, name='developpement_web'),
    url(r'^accueil/dev_mobil/$', views.dev_mobil, name='developpement_mobil'),
    url(r'^accueil/automatisation/$', views.automatisation, name='automatisation_taches'),
    url(r'^accueil/portefeuil/$', views.portefeuil, name='portefeuil'),
    url(r'^accueil/presentation/$', views.presentation, name='presentation'),
    url(r'^accueil/login/$', views.login, name='login'),
    url(r'^accueil/login/projet/$', views.login, name='projet'),
    url(r'^accueil/contact/$', views.contact, name='contact'),
]
