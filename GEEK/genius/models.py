# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


# Create your models here.

class User_geek(models.Model):
    """
    la tables des utilisatuer desirants une formation
    """
    nom = models.CharField(max_length=50, verbose_name="Nom", help_text="Votre nom")
    prenom = models.CharField(max_length=100, verbose_name="Prenom")
    contact = models.CharField(max_length=8, verbose_name="Contact(s)")
    email = models.CharField(max_length=30, verbose_name="E-mail")
    adresse = models.CharField(max_length=30, verbose_name="Adresse")
    password_user = models.CharField(max_length=15, verbose_name="Mot de passe")
    date = models.DateField(default=timezone.now, blank=True,
                            verbose_name="Date de création")
    photo = models.ImageField(upload_to='images', default=0, verbose_name="Choisir une photo")

    class Meta:
        unique_together = (('email', 'password_user'),)

    def __str__(self):
        """
        description sur un nom du model
        :return: 
        """
        return '%s, %s' % (self.nom, self.prenom)
