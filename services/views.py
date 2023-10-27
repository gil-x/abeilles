import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Category
from .forms import ServiceForm, CategoryForm, CategoryForm2
from pages.models import PageServices, PageServicesPro, PageServicesInd
# from questions.models import QuestionServicesInd, QuestionServicesPro
from settings.models import ContactEmail, RecipientEmail
from questions.models import (
        QuestionServicesInd, QuestionServicesPro,
    )
from honeypot.decorators import check_honeypot

from django.contrib import messages

# def index(request):
#     context = {}
#     context["page_class"] = "packages"
#     context["packages"] = []

#     for app_type in Package.AppTypes:
#         packages_part = (
#             app_type.label, Package.objects.filter(app_type=app_type))
#         context["packages"].append(packages_part)

#     return render(request, 'packages/index.html', context)

# for services in Category.name:


# {% regroup services by category as groups %}
# {% for group in groups %}
# {% endfor %}


def index(request):
    
    page = PageServices.objects.first()
    services_professionnels = []
    services_particuliers = []

    for category in Category.objects.all():
        pro_services_by_category = Service.objects.filter(
                category__target="PROFESSIONNEL",
                category=category,
            )
        pro_services_by_category_count = pro_services_by_category.count()
        if pro_services_by_category_count > 0:
            services_professionnels.append(pro_services_by_category)

    for category in Category.objects.all():
        ind_services_by_category = Service.objects.filter(
                category__target="PARTICULIER",
                category=category,
            )
        ind_services_by_category_count  = ind_services_by_category.count()
        if ind_services_by_category_count > 0:
            services_particuliers.append(ind_services_by_category)

    context = {
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
        "services_professionnels": services_professionnels,
        "services_particuliers": services_particuliers,
        "page_class": "services",
    }

    return render(request, 'services/index.html', context)


@check_honeypot(field_name='firstname')
def category(request, category_slug):

    category = Category.objects.get(slug=category_slug)
    services = Service.objects.filter(
            category=category,
            available=True,
        )
    if category.target == "PARTICULIER":
        questions = QuestionServicesInd.objects.all()
    else:
        questions = QuestionServicesPro.objects.all()

    context = {
        "meta_title": category.meta_title,
        "meta_description": category.meta_description,
        "title": category.title,
        "headline": category.headline,
        "featured_image": category.featured_image,
        "body1": category.body1,
        "image1": category.image1,
        "services": services,
        "page_class": f"service category {category.target.lower()}",
        "meta_title": f"prestation de service : {category.title.lower()}",
        "questions": questions,
    }

    if request.method == 'POST':
        context["form_category"] = CategoryForm2(
                request.POST,
                s_category=category.id,
            )
        # Form is valid
        if context["form_category"].is_valid():
            # Get Email for sending and recipients emails 
            sender = ContactEmail.objects.first()
            recipients = [ recipient.email for recipient in RecipientEmail.objects.all() ]
            # Get message elements:
            name = context["form_category"].cleaned_data['name']
            company = context["form_category"].cleaned_data['company']
            email = context["form_category"].cleaned_data['email']

            extra_services = list(context["form_category"].cleaned_data['extra_services'])

            # Message for Abeilles
            if extra_services:
                extra_services_text = f"""
Le(s) service(s) suivants m'intéress(ent) particulièrement :
{ ', '.join([service.name for service in extra_services]) }
"""
            else:
                extra_services_text = ""
            message = f"""
Message de {email},
Demande de service envoyée le {datetime.datetime.now()},
Catégorie de services demandée : {category.name}
{extra_services_text}
--
Nom : {name}
Société : {company}
Email : {email}
"""         
            # Send Email to Abeilles
            for mail in recipients:
                send_mail(f"[Demande de service] {category.name}", message, sender.email, [mail])

            # Message for User
            if extra_services:
                extra_services_text = f"""
Le(s) service(s) suivants qui vous intéress(ent) particulièrement :
{ ', '.join([service.name for service in extra_services]) }
"""
            else:
                extra_services_text = ""
            message = f"""
Merci pour votre demande de service !
Voici la demande que vous avez formulée le {datetime.datetime.now()} :

Catégorie de services demandée : {category.name}
{extra_services_text}
--
Nom : {name}
Société : {company}
Email : {email}
"""
            # Senf copy to User
            recipients = [email]
            for mail in recipients:
                send_mail("Votre demande de service", message, sender.email, [mail])
            context["form_category"] = CategoryForm2(
                    s_category=category.id,
                )
            messages.success(request, "Votre demande a bien été envoyée")
            render(request, 'services/category.html', context)
        # Form not not valid
        else:
            messages.error(request, "Il y a eu un problème, veuillez réessayer")
            render(request, 'services/category.html', context)
    else:
        context["form_category"] = CategoryForm2(
            s_category=category.id,
        )
    return render(request, 'services/category.html', context)


def service(request, service_slug):
    """
    NOT USED
    """
    context = {}
    context["service"] = Service.objects.get(slug=service_slug)
    context["page_class"] = "service",

    if request.method == 'POST':
        context["form"] = ServiceForm(
                request.POST,
                s_category=context["service"].category.id,
                excluded_id=context["service"].id,
            )
        # Form is valid
        if context["form"].is_valid():
            sender = ContactEmail.objects.first()
            subject = "Demande de service"
            name = context["form"].cleaned_data['name']
            company = context["form"].cleaned_data['company']
            email = context["form"].cleaned_data['email']
            extra_services = list(context["form"].cleaned_data['extra_services'])
            message = f"""
Message de {email},
Demande de service envoyée le {datetime.datetime.now()},
--
Nom : {name}
Société : {company}
Email : {email}
Le(s) service(s) suivants m'intéress(ent) aussi par :
{ ', '.join([service.name for service in extra_services]) }
""" 
            recipients = [email, sender.email]
            for mail in recipients:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [mail])
            messages.success(request, "Votre demande a bien été envoyée")
            render(request, 'services/single.html')
        # Form not not valid
        else:
            messages.error(request, "Il y a eu un problème, veuillez réessayer")
            render(request, 'services/single.html', context)
    else:
        print(f"***\ncontext['service'].category.id: { context['service'].category.id }\n***")
        context["form"] = ServiceForm(
                s_category=context["service"].category.id,
                excluded_id=context["service"].id
            )

    return render(request, 'services/single.html', context)


# Attempts

# def services_pro(request):
    
#     page = PageServicesPro.objects.first()
#     services_professionnels = []

#     for category in Category.objects.all():
#         pro_services_by_category = Service.objects.filter(
#                 category__target="PROFESSIONNEL",
#                 category=category,
#             )
#         pro_services_by_category_count = pro_services_by_category.count()
#         if pro_services_by_category_count > 0:
#             services_professionnels.append(pro_services_by_category)

#     context = {
#         "meta_title": page.meta_title,
#         "meta_description": page.meta_description,
#         "title": page.title,
#         "headline": page.headline,
#         "featured_image": page.featured_image,
#         "body1": page.body1,
#         "image1": page.image1,
#         "body2": page.body2,
#         "image2": page.image2,
#         "body3": page.body3,
#         "image3": page.image3,
#         "services_professionnels": services_professionnels,
#         "page_class": "services-pro",
#     }

#     return render(request, 'services/index-pro.html', context)


# def services_ind(request):
    
#     page = PageServicesInd.objects.first()
#     services_particuliers = []

#     for category in Category.objects.all():
#         ind_services_by_category = Service.objects.filter(
#                 category__target="PARTICULIER",
#                 category=category,
#             )
#         ind_services_by_category_count  = ind_services_by_category.count()
#         if ind_services_by_category_count > 0:
#             services_particuliers.append(ind_services_by_category)

#     context = {
#         "meta_title": page.meta_title,
#         "meta_description": page.meta_description,
#         "title": page.title,
#         "headline": page.headline,
#         "featured_image": page.featured_image,
#         "body1": page.body1,
#         "image1": page.image1,
#         "body2": page.body2,
#         "image2": page.image2,
#         "body3": page.body3,
#         "image3": page.image3,
#         "services_particuliers": services_particuliers,
#         "page_class": "services-ind",
#     }

#     return render(request, 'services/index-ind.html', context)