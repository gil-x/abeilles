from django.conf import settings
from django.shortcuts import render, get_object_or_404
# from .models import (
#         Page, Homepage,
#         PageAssociation, PageTeam, PageMissions, PageValues, PagePartners,
#         PageMissions, PageValues, PagePartners, PageJobhunt,
#         PageGarden, PageGardenProject,
#         PageServices, PageServicesInd, PageServicesPro,
#     )
from .models import (
        Page, Homepage,
        PageAssociation, PageMissions, PageTerritorialInfluence,
        PageMissions, PageJobhunt,
        PageGarden, PageGardenProject,
        PageServices, PageServicesInd, PageServicesPro,
    )
from settings.models import ContactEmail, RecipientEmail
from services.models import Service, Category
from posts.models import Post
from basket.forms import NewsletterForm
import requests
import json

from honeypot.decorators import check_honeypot

from django.core.mail import send_mail
from .forms import ContactForm, JobSearchForm, GardenForm
from questions.models import (
        QuestionServicesInd, QuestionServicesPro, QuestionGarden
    )
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

def page_services_pro(request):
    # context = {}

    services_professionnels = []
    for category in Category.objects.all():
        pro_services_by_category = Service.objects.filter(
                category__target="PROFESSIONNEL",
                category=category,
            )
        pro_services_by_category_count = pro_services_by_category.count()
        if pro_services_by_category_count > 0:
            services_professionnels.append(pro_services_by_category)

    page = PageServicesPro.objects.first()
    questions = QuestionServicesPro.objects.all()
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
        "page_class": "garden",
        "questions": questions,

        "testimony_title":page.testimony_title,
        "testimony1_image": page.testimony1_image,
        "testimony1_name": page.testimony1_name,
        "testimony1_text": page.testimony1_text,
        "testimony2_image": page.testimony2_image,
        "testimony2_name": page.testimony2_name,
        "testimony2_text": page.testimony2_text,
        "testimony3_image": page.testimony3_image,
        "testimony3_name": page.testimony3_name,
        "testimony3_text": page.testimony3_text,

        "services_professionnels": services_professionnels,

        "page_class": "services-pro",
    }
    return render(request, f'pages/services-pro.html', context)


def page_services_ind(request):
    # context = {}
    services_particuliers = []

    for category in Category.objects.all():
        ind_services_by_category = Service.objects.filter(
                category__target="PARTICULIER",
                category=category,
            )
        ind_services_by_category_count  = ind_services_by_category.count()
        if ind_services_by_category_count > 0:
            services_particuliers.append(ind_services_by_category)

    page = PageServicesInd.objects.first()
    questions = QuestionServicesInd.objects.all()
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
        "page_class": "garden",
        "questions": questions,

        "testimony_title":page.testimony_title,
        "testimony1_image": page.testimony1_image,
        "testimony1_name": page.testimony1_name,
        "testimony1_text": page.testimony1_text,
        "testimony2_image": page.testimony2_image,
        "testimony2_name": page.testimony2_name,
        "testimony2_text": page.testimony2_text,
        "testimony3_image": page.testimony3_image,
        "testimony3_name": page.testimony3_name,
        "testimony3_text": page.testimony3_text,

        "services_particuliers": services_particuliers,

        "page_class": "services-ind",
    }
    return render(request, f'pages/services-ind.html', context)

@check_honeypot(field_name='firstname')
def page_garden(request):
    context = {}
    page = PageGarden.objects.first()
    questions = QuestionGarden.objects.all()
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
        "page_class": "garden",
        "questions": questions,

        "testimony_title":page.testimony_title,
        "testimony1_image": page.testimony1_image,
        "testimony1_name": page.testimony1_name,
        "testimony1_text": page.testimony1_text,
        "testimony2_image": page.testimony2_image,
        "testimony2_name": page.testimony2_name,
        "testimony2_text": page.testimony2_text,
        "testimony3_image": page.testimony3_image,
        "testimony3_name": page.testimony3_name,
        "testimony3_text": page.testimony3_text,
    }

    if request.method == 'POST':
        context["form_garden"] = GardenForm(request.POST)
        # Form is valid
        if context["form_garden"].is_valid():
            # Get Email for sending and recipients emails 
            sender = ContactEmail.objects.first()
            recipients = [ recipient.email for recipient in RecipientEmail.objects.all() ]
            # Get message elements:
            name = context["form_garden"].cleaned_data['name']
            email = context["form_garden"].cleaned_data['email']
            phone = context["form_garden"].cleaned_data['phone']
            copy = context["form_garden"].cleaned_data['copy']

            message = f"""
Nom : {name}
Email : {email},
Téléphone : {phone},
via le formulaire de contact.
--
            
{context["form_garden"].cleaned_data['message']}""" 
            # No copy asked:
            for mail in recipients:
                send_mail("[A propos du jardin]", message, sender.email, [mail])
            # Copy asked:
            if copy:
                copy_message = """
Votre message a bien été transmis
*** copie ci-dessous

"""
                message = copy_message + message
                send_mail(f"[copie] Votre question sur le jardin", message, sender.email, [email])

            messages.success(request, "Merci pour votre message !")
            context["form_garden"] = GardenForm()
            # context["form_submitted"] = True

            return render(request, 'pages/garden.html', context)
        # Form not not valid
        else:
            messages.error(request, "Il y a eu un problème, veuillez réessayer")
            return render(request, 'pages/hello_bot.html', context)
    # Request is not POST
    else:
        context["form_garden"] = GardenForm()
    return render(request, f'pages/garden.html', context)


def page_garden_project(request):
    context = {}
    page = PageGardenProject.objects.first()
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
        "page_class": "garden-project",
    }
    return render(request, f'pages/garden-project.html', context)


@check_honeypot(field_name='firstname')
def page_jobhunt(request):
    context = {}
    page = PageJobhunt.objects.first()
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
        "job_body_extra": page.body_extra,
        "job_image_extra": page.image_extra,
        "page_class": "jobhunt",

        "testimony_title":page.testimony_title,
        "testimony1_image": page.testimony1_image,
        "testimony1_name": page.testimony1_name,
        "testimony1_text": page.testimony1_text,
        "testimony2_image": page.testimony2_image,
        "testimony2_name": page.testimony2_name,
        "testimony2_text": page.testimony2_text,
        "testimony3_image": page.testimony3_image,
        "testimony3_name": page.testimony3_name,
        "testimony3_text": page.testimony3_text,
    }
    if request.method == 'POST':
        context["form_jobhunt"] = JobSearchForm(request.POST)
        # Form is valid
        if context["form_jobhunt"].is_valid():
            # Get Email for sending and recipients emails 
            sender = ContactEmail.objects.first()
            recipients = [ recipient.email for recipient in RecipientEmail.objects.all() ]
            # Get message elements:
            name = context["form_jobhunt"].cleaned_data['name']
            email = context["form_jobhunt"].cleaned_data['email']
            phone = context["form_jobhunt"].cleaned_data['phone']
            location = context["form_jobhunt"].cleaned_data['location']
            copy = context["form_jobhunt"].cleaned_data['copy']

            message = f"""
Nom : {name}
Email : {email},
Téléphone : {phone},
Lieu de résidence : {location},
via le formulaire de contact.
--
            
{context["form_jobhunt"].cleaned_data['message']}""" 
            # No copy asked:
            for mail in recipients:
                send_mail("[Demandeur d'emploi]", message, sender.email, [mail])
            # Copy asked:
            if copy:
                copy_message = """
Votre message a bien été transmis
*** copie ci-dessous

"""
                message = copy_message + message
                send_mail(f"[copie] Votre demande d'emploi", message, sender.email, [email])

            messages.success(request, "Votre message a bien été envoyé.")
            context["form_jobhunt"] = JobSearchForm()
            # context["form_submitted"] = True

            return render(request, 'pages/jobhunt.html', context)
        # Form not not valid
        else:
            messages.error(request, "Il y a eu un problème, veuillez réessayer")
            return render(request, 'pages/hello_bot.html', context)
    # Request is not POST
    else:
        context["form_jobhunt"] = JobSearchForm()
    return render(request, f'pages/jobhunt.html', context)


def page_association(request):
    context = {}
    page = PageAssociation.objects.first()
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
        "page_class": "association",
    }
    return render(request, f'pages/association.html', context)


# def page_team(request):
#     context = {}
#     page = PageTeam.objects.first()
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
#         "page_class": "team",
#     }
#     return render(request, f'pages/team.html', context)


def page_missions(request):
    context = {}
    page = PageMissions.objects.first()
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
        "page_class": "missions",
    }
    return render(request, f'pages/missions.html', context)


def page_territorial_influence(request):
    context = {}
    page = PageTerritorialInfluence.objects.first()
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
        "page_class": "territorial-influence",
    }
    return render(request, f'pages/values.html', context)

# def page_values(request):
#     context = {}
#     page = PageValues.objects.first()
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
#         "page_class": "values",
#     }
#     return render(request, f'pages/values.html', context)


# def page_partners(request):
#     context = {}
#     page = PagePartners.objects.first()
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
#         "page_class": "partners",
#     }
#     return render(request, f'pages/partners.html', context)


def page_custom(request, page_slug):
    context = {}
    page = get_object_or_404(Page, slug=page_slug)

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
        }

    if page.role == "GARDEN":
        if request.method == 'POST':
            # Newsletter form
            context["form"] = NewsletterForm(request.POST)
            # Form is valid
            if context["form"].is_valid(): 
                firstname = context["form"].cleaned_data['firstname']
                lastname = context["form"].cleaned_data['lastname']
                email = context["form"].cleaned_data['email']
                basket_subscription = context["form"].cleaned_data['basket_subscription']
                aai_subscription = context["form"].cleaned_data['aai_subscription']

                lists = []

                if basket_subscription:
                    lists.append(2)

                if aai_subscription:
                    lists.append(3)

                url = "https://api.sendinblue.com/v3/contacts/doubleOptinConfirmation"
                redirection_url = f"{ request.scheme }://{ get_current_site(request).domain }{ request.get_full_path() }"

                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "api-key": settings.SENDINGBLUE_API_KEY
                }

                data = {
                    "attributes": {
                        "PRENOM": firstname,
                        "NOM": lastname
                    },
                    "templateId": 2,
                    "includeListIds": lists,
                    "email": email,
                    "redirectionUrl": redirection_url
                }

                response = requests.post(url, data=json.dumps(data), headers=headers)
                
                return render(request, 'basket/thanks.html')
            # Form not not valid
            else:
                context["error"] = "True"
        # Request is not POST
        else:
            context["form"] = NewsletterForm()

    if page.role == "JOBHUNT":
        if request.method == 'POST':
            context["form"] = JobSearchForm(request.POST)
            if context["form"].is_valid():
                name = context["form"].cleaned_data['name']
                email = context["form"].cleaned_data['email']
                message  = context["form"].cleaned_data['message']
                return render(request, 'basket/thanks.html')
            # Form not not valid
            else:
                context["error"] = "True"
        # Request is not POST
        else:
            context["form"] = JobSearchForm()

    if page.role == "SERVICES_PRO":
        context["pro_services_set"] = []
        for category in Category.objects.all():
            services = Service.objects.filter(category__target="PROFESSIONNEL", category=category)
            context["pro_services_set"].append([service for service in services])

    elif page.role == "SERVICES_IND":
        context["ind_services_set"] = []
        for category in Category.objects.all():
            services = Service.objects.filter(category__target="PARTICULIER", category=category)
            context["ind_services_set"].append([service for service in services])

    return render(request, f'pages/{page.role.lower()}.html', context)


def homepage(request, **kwargs):
    context = {}
    page = get_object_or_404(Homepage)
    # pro_services_set = []
    # ind_services_set = []
    services_professionnels = []
    services_particuliers = []
    posts = Post.objects.filter(promoted=True).order_by("updated_at")[:3]
    # for category in Category.objects.all():
    #     services = Service.objects.filter(category__target="PROFESSIONNEL", category=category)
    #     pro_services_set.append([service for service in services])
    # for category in Category.objects.all():
    #     services = Service.objects.filter(category__target="PARTICULIER", category=category)
    #     ind_services_set.append([service for service in services])
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
        "page": page,
        "services_professionnels": services_professionnels,
        "services_particuliers": services_particuliers,
        "posts": posts,
        "meta_title": page.meta_title,
        "meta_description": page.meta_description,
        "page_class": "home",
    }
    if request.GET.get('newsletter') == 'ok':
        # context["nl_subscription"] = True
        messages.success(request, "Merci pour votre intérêt ! Vous allez recevoir un email avec un lien pour confirmer votre abonnement.")
    return render(request, f'pages/homepage.html', context)


@check_honeypot(field_name='firstname')
def contact(request):
    context = {
        "meta_title": "Contacter l'association Abeilles Aide et Entraide",
        "meta_description": "Abeilles Aide et Entraide - contactez-nous au 01 69 42 31 10.",
        "page_class": "contact",
    }

    if request.method == 'POST':
        context["form"] = ContactForm(request.POST)
        # Form is valid
        if context["form"].is_valid():
            # Get Email for sending and recipients emails 
            sender = ContactEmail.objects.first()
            recipients = [ recipient.email for recipient in RecipientEmail.objects.all() ]
            # Get message elements:
            name = context["form"].cleaned_data['name']
            customer_types = ['particulier', 'professionnel']
            customer_type = customer_types [ int(context["form"].cleaned_data['type']) - 1]
            if customer_type == 'particulier':
                subject = context["form"].cleaned_data['subject_ind']
            elif customer_type == 'professionnel':
                subject = context["form"].cleaned_data['subject_pro']
            else:
                subject = "Sujet non défini"
            email = context["form"].cleaned_data['email']
            phone = context["form"].cleaned_data['phone']
            copy = context["form"].cleaned_data['copy']

            message = f"""
Nom : {name}
Email : {email},
Téléphone : {phone},
via le formulaire de contact.
--
            
{context["form"].cleaned_data['message']}""" 
            # No copy asked:
            for mail in recipients:
                send_mail(f"[Contact {customer_type}] {subject}", message, sender.email, [mail])
            # Copy asked:
            if copy:
                copy_message = """
Votre message a bien été transmis
*** copie ci-dessous

"""
                message = copy_message + message
                send_mail(f"[copie] {subject}", message, sender.email, [email])

            messages.success(request, "Merci pour votre message !")
            context["form"] = ContactForm()
            # context["form_submitted"] = True
            return render(request, 'pages/contact.html', context)
        # Form not not valid
        else:
            # context["error"] = "True"
            messages.error(request, "Il y a eu un problème, veuillez réessayer")
            return render(request, 'pages/hello_bot.html', context)
    else:
        context["form"] = ContactForm()
        return render(request, 'pages/contact.html', context)
