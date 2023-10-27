from django import forms
from .models import Basket

  
class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = "__all__"
        # fields = ['total', 'booked']


class NewsletterForm(forms.Form):
    """
    Newsletter subscription. Available in Garden page.
    """
    firstname = forms.CharField(
            max_length=30,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Prénom"}),
        )
    lastname = forms.CharField(
            max_length=30,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Nom"}),
        )
    # message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre adresse e-mail"}),
        )
    basket_subscription = forms.BooleanField(label="Je veux recevoir les infos sur le panier", required=False)
    aai_subscription = forms.BooleanField(label="Je veux en savoir plus sur les Abeilles", required=False)


class BasketDemandForm(forms.Form):
    """
    Basket subscription for customers.
    """
    name = forms.CharField(
            max_length=100,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre nom"}),
        )
    email = forms.EmailField(
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre adresse e-mail"})
        )


class TestForm(forms.Form):
    word = forms.CharField(max_length=100, label="Word")