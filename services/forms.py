import datetime
from django import forms
from django.forms.widgets import TextInput, EmailInput
from django.http import request 
from .models import Category, Service
from django.db.models import Q


class BaseServiceForm(forms.Form):
 
    # service = forms.CharField(
    #         max_length=50,
    #         widget=forms.HiddenInput()
    # )

    
    # Vos coordonées
    name = forms.CharField(
            max_length=30,
            label="",
            widget=forms.TextInput(attrs={'placeholder': f'Votre nom*'}),
        )
    location = forms.CharField(
            max_length=30,
            label="",
            widget=forms.TextInput(attrs={'placeholder': 'Ville d\'intervention*'}),
        )
    company = forms.CharField(
            max_length=20,
            label="",
            widget=forms.TextInput(attrs={'placeholder': 'Votre entreprise*'}),
            required=False,
        )
    email = forms.EmailField(
            label="",
            widget=forms.EmailInput(attrs={'placeholder': 'Votre email'}),
            required=False,
        )
    phone = forms.CharField(
            max_length=20,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Numéro de téléphone*"})
        )

    # def __init__(self, exclude_id):
    #     super().__init__()

    #     print('\n****\n', 'yo', '\n****\n',)
    #     self.fields['extra_services'] = forms.ModelMultipleChoiceField(
    #     label=f"J'ai aussi besoin de ...",
    #     queryset=Service.objects.filter(target="PARTICULIER", available=True).exclude(id=3),
    #     widget=forms.CheckboxSelectMultiple,
    #     initial=0,
    # )

    extra_services = forms.ModelMultipleChoiceField(
            # label=f"J'ai surtout besoin de...",
            queryset=Service.objects.filter(category__target="PARTICULIER", available=True),
            widget=forms.CheckboxSelectMultiple,
            initial=0,
        )
    


class ServiceForm(BaseServiceForm):
    def __init__(self, *args, s_category, excluded_id, **kwargs):
        # self.excluded_id = excluded_id

        super().__init__(*args, **kwargs)
        self.fields['extra_services'] = forms.ModelMultipleChoiceField(
            label=f"J'ai aussi besoin de...",
            queryset=Service.objects.filter(
                    # category__target="PARTICULIER",
                    available=True,
                    category=s_category,
                    ).exclude(id=excluded_id),
            widget=forms.CheckboxSelectMultiple,
            initial=0,
        )


class CategoryForm(forms.Form):
    # Vos coordonées
    name = forms.CharField(
            max_length=20,
            label="",
            widget=forms.TextInput(attrs={'placeholder': f'Votre nom*'}),
        )
    company = forms.CharField(
            max_length=20,
            label="",
            widget=forms.TextInput(attrs={'placeholder': 'Votre entreprise*'}),
        )
    email = forms.EmailField(
            label="",
            widget=forms.EmailInput(attrs={'placeholder': 'Votre email'}),
            required=False,
        )
    


class CategoryForm2(BaseServiceForm):
    def __init__(self, *args, s_category, **kwargs):
        # self.excluded_id = excluded_id

        super().__init__(*args, **kwargs)
        self.fields['extra_services'] = forms.ModelMultipleChoiceField(
            label=f"J'ai besoin de ...",
            required=False,
            queryset=Service.objects.filter(
                    # category__target="PARTICULIER",
                    available=True,
                    category=s_category,
                    ),
            widget=forms.CheckboxSelectMultiple,
            initial=0,
        )
