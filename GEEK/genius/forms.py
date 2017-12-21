# -*- coding:utf-8 -*-

from django import forms

from .models import User_geek
from django.contrib.auth.models import User


class userForm_geek(forms.ModelForm):
    """
    formulaire de l'utilisateur
    """

    class Meta:
        """
        les champs nécessaires
        """
        model = User_geek
        fields = ('nom', 'prenom', 'contact', 'email', 'password_user')


class UserForm(forms.ModelForm):
    """
    ecriture du formulaire de connexion de l'utilisateur
    """

    class Meta:
        """
        les champs visible dans le formulaire
        """
        model = User
        fields = ('username', 'password')
