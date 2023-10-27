from django.conf import settings

import requests
import json

from django.shortcuts import render, redirect
from .models import Basket
from .forms import BasketForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.sites.shortcuts import get_current_site

# Test ajax form:
from .forms import NewsletterForm, BasketDemandForm
from django.views.generic import FormView
from django.http import JsonResponse

from settings.models import NewsletterConfig
# from django.urls import reverse, reverse_lazy

from pages.models import PageBasket
from questions.models import QuestionGarden

from honeypot.decorators import check_honeypot
from settings.models import ContactEmail, RecipientEmail
from django.core.mail import send_mail

from django.contrib import messages

@check_honeypot(field_name='firstname')
def index(request):
    page = PageBasket.objects.first()
    questions = QuestionGarden.objects.all()
    context = {
        "basket": Basket.objects.first(),
        "meta_title": page.meta_title,
        "meta_description": page.meta_description,
        "title": page.title,
        "headline": page.headline,
        "featured_image": page.featured_image,
        "body1": page.body1,
        "image1": page.image1,
        "body2": page.body2,
        "image2": page.image2,
        "body3": page.body3,
        "image3": page.image3,
        "direct_sale": page.body_extra,
        "page_class": "basket",
        "questions": questions,
        "body_food": page.body_food,
    }

    if request.method == 'POST':
        context["basket_static_form"] = BasketDemandForm(request.POST)
        # Form is valid
        if context["basket_static_form"].is_valid():
            # Get Email for sending and recipients emails 
            sender = ContactEmail.objects.first()
            recipients = [ recipient.email for recipient in RecipientEmail.objects.all() ]
            name = context["basket_static_form"].cleaned_data['name']
            email = context["basket_static_form"].cleaned_data['email']
            message = f"""
Nom : {name}
Email : {email}
""" 
            for mail in recipients:
                send_mail(f"[Abonnement Paniers]", message, sender.email, [mail])
            context["basket_static_form"] = BasketDemandForm()
            # context["form_submitted"] = True
            messages.success(request, "Votre demande a bien été envoyée. Nous vous contacterons très prochainement.")
            return render(request, 'basket/index.html')
        # Form not not valid
        else:
            # context["error"] = "True"
            messages.error(request, "Il y a eu un problème, veuillez réessayer")
            return render(request, 'basket/index.html', context)
    else:
        context["basket_static_form"] = BasketDemandForm()
        return render(request, 'basket/index.html', context)


@login_required
def edit(request):
    context = {}
    basket= Basket.objects.first()
    context['form'] = BasketForm(request.POST or None, instance= basket)
    context["page_class"] = "basket edit"

    if request.method == 'POST':

        if context['form'].is_valid():
            print('valid')
            basket= context['form'].save(commit= False)
            basket.save()
            return redirect('basket')
        
    return render(request, "basket/edit.html", context)


class Thanks(TemplateView):
    template_name = "basket/thanks.html"


def subcription_endpoint(request):
    if request.method == 'POST':
        form = NewsletterForm(json.loads(request.body))
        nl_config = NewsletterConfig.objects.first()
        print(f"nl_config key: {nl_config.sendingblue_api_key}")
        print(f"nl_config smtp: {nl_config.sendingblue_smtp_key}")

        # Form is valid
        if form.is_valid(): 
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            basket_subscription = form.cleaned_data['basket_subscription']
            aai_subscription = form.cleaned_data['aai_subscription']

            lists = []
            if basket_subscription:
                lists.append(2)
            if aai_subscription:
                lists.append(3)

            url = "https://api.sendinblue.com/v3/contacts/doubleOptinConfirmation"
            redirection_url = f"{ request.scheme }://{ get_current_site(request).domain }/?newsletter=ok"

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "api-key": nl_config.sendingblue_api_key
            }

            data = {
                "attributes": {
                    "PRENOM": firstname,
                    "NOM": lastname
                },
                "templateId": 3,
                "includeListIds": lists,
                "email": email,
                "redirectionUrl": redirection_url
            }

            response = requests.post(url, data=json.dumps(data), headers=headers)

            if response.ok:
                return JsonResponse({"success": True}, status=200)
            else:
                return JsonResponse(
                        {"success": False, "response": response.text},
                        status=400,
                    )
        # Form not not valid
        else:
            return JsonResponse({"success": False}, status=200)
