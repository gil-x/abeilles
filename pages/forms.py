from django import forms


class ContactForm(forms.Form):
    """
    Simple contact form. Available in Contact Page.
    """
    name = forms.CharField(
            max_length=100,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre nom / Raison Sociale"})
        )
    type = forms.ChoiceField(
            widget=forms.RadioSelect,
            label="Vous êtes :",
            choices=[
                    ('1', 'Un particulier'),
                    ('2', 'Un professionnel'),
                ],
        )
    subject_pro = forms.CharField(
            max_length=100,
            label="",
            required=False,
            widget=forms.TextInput(attrs={
                    "placeholder":"Suggestions de sujet pour les professionnels",
                    "required": False,
                })
        )
    subject_ind = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        label="Sujet",
        choices=[
            ('Question', 'Question'),
            ('Service', 'Service'),
            ('Vente légumes', 'Vente légumes'),
            ('Autres', 'Autres'),
        ],
        initial=0,
    )
    email = forms.EmailField(
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre adresse e-mail"})
        )
    phone = forms.CharField(
            max_length=20,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Numéro de téléphone"})
        )
    message = forms.CharField(
            label="",
            widget=forms.Textarea(attrs={"placeholder":"Message"})
        )
    copy = forms.BooleanField(label="Recevoir une copie", required=False)

    # class LoginForm(forms.Form):
    # username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'username'}))
    # password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'password'}))


class JobSearchForm(forms.Form):
    # subject = forms.CharField(max_length=100, label="Sujet")
    name = forms.CharField(
            max_length=100,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre nom"})
        )
    email = forms.EmailField(
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre adresse e-mail"})
        )
    phone = forms.CharField(
            max_length=20,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Numéro de téléphone"})
        )
    location = forms.CharField(
            max_length=30,
            label="",
            widget=forms.TextInput(attrs={'placeholder': 'Ville de résidence*'}),
        )
    message = forms.CharField(
            label="",
            widget=forms.Textarea(attrs={"placeholder":"Message"})
        )
    copy = forms.BooleanField(label="Recevoir une copie", required=False)


class SpecialServiceForm(forms.Form):
    subject = forms.CharField(
            max_length=100,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Sujet"})
        )
    message = forms.CharField(
            label="",
            widget=forms.Textarea(attrs={"placeholder":"Message"})
        )
    email = forms.EmailField(
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre adresse e-mail"})
        )
    copy = forms.BooleanField(label="Recevoir une copie", required=False)


class GardenForm(forms.Form):
    """
    Simple contact form. Available in Garden Page.
    """
    name = forms.CharField(
            max_length=100,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre nom"})
        )
    email = forms.EmailField(
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Votre adresse e-mail"})
        )
    phone = forms.CharField(
            max_length=20,
            label="",
            widget=forms.TextInput(attrs={"placeholder":"Numéro de téléphone"})
        )
    message = forms.CharField(
            label="",
            widget=forms.Textarea(attrs={"placeholder":"Message"})
        )
    copy = forms.BooleanField(label="Recevoir une copie", required=False)