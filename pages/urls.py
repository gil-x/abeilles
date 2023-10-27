from pages.models import Homepage
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # AAE
    path('association', views.page_association, name='association'),
    # path('notre-equipe', views.page_team, name='team'),
    path('missions-valeurs-engagement', views.page_missions, name='missions'),
     path('rayonnement-territorial', views.page_territorial_influence, name='territorial-influence'),
    # path('nos-valeurs', views.page_values, name='values'),
    # path('nos-partenaires', views.page_partners, name='partners'),
    # garden
    path('jardin', views.page_garden, name='garden'),
    path('jardin/projet', views.page_garden_project, name='garden-project'),
    # jobhunt
    path('demandeur-emploi', views.page_jobhunt, name='jobhunt'),
    # services
    path('services-pour-professionnels', views.page_services_pro, name='services_pro'),
    path('services-pour-particuliers', views.page_services_ind, name='services_ind'),
    # contact
    path('contact', views.contact, name='contact'),
    # static pages
    path('cookies', TemplateView.as_view(
            template_name='pages/cookies.html',
            extra_context={
                "full_text_page": True,
            }), name="cookies"),
    path('confidentiality', TemplateView.as_view(
            template_name='pages/confidentiality.html',
            extra_context={
                "full_text_page": True,
            }), name="confidentiality"),
    path('mentions-legales', TemplateView.as_view(
            template_name='pages/legal-notice.html',
            extra_context={
                "full_text_page": True,
            }), name="legal-notice"),
    # not used
    # path('<page_slug>/', views.page_custom, name='page'),
]
