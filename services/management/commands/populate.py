import random

from django.apps.registry import apps
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from services.models import Category, Service
# from pages.models import (
#         Homepage,
#         PageServices, PageServicesPro, PageServicesInd,
#         PageAssociation, PageTeam, PageMissions, PageValues, PagePartners,
#         PageGarden, PageGardenProject, PageBasket,
#         PageJobhunt,
#     )
from pages.models import (
        Homepage,
        PageServicesPro, PageServicesInd,
        PageAssociation, PageMissions, PageTerritorialInfluence,
        PageGarden, PageGardenProject, PageBasket,
        PageJobhunt,
    )
from posts.models import Post
from basket.models import Basket
from questions.models import QuestionServicesPro, QuestionServicesInd, QuestionGarden
from settings.models import ContactEmail, NewsletterConfig, RecipientEmail, SocialLinks

from django.conf import settings
import os

LOREM_IPSUM = [
    "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam viverra augue ex. Suspendisse venenatis ullamcorper magna, sed faucibus magna viverra ut. Pellentesque porta sem vel velit rhoncus congue vitae tincidunt justo.</p>",

    "<p>Vivamus molestie mauris a nunc suscipit, nec porta augue vulputate. Nullam at viverra tellus. Vestibulum tincidunt, lectus ut feugiat bibendum, erat diam laoreet risus, vitae bibendum mi purus vel enim. Pellentesque a ultrices elit.</p>",

    "<p>Maecenas lobortis dignissim erat nec aliquet. Vestibulum id mattis purus. Donec dignissim ultricies placerat. Cras quis eros nec libero interdum aliquet. Curabitur orci dolor, malesuada in egestas non, tempor in eros. Aliquam aliquet dolor a neque hendrerit fringilla.</p>",

    "<p>Phasellus sit amet ligula at quam luctus consectetur. Fusce et felis at ligula luctus sollicitudin id id ipsum. Etiam porttitor, nulla eu pretium aliquam, nisi quam vehicula urna, sit amet pellentesque felis dui et nisi.</p>",

    "<p>Phasellus ullamcorper tellus nec orci pellentesque ullamcorper. Duis feugiat, eros eu suscipit mattis, risus sem bibendum ex, vel consectetur neque mauris a erat.</p>",

    "<p>Vivamus luctus diam nec accumsan scelerisque. Donec sit amet feugiat sem. Aliquam lacinia, ligula sed condimentum commodo, nulla ex molestie mi, ac tempor tortor massa id turpis. Sed interdum eleifend dictum. Maecenas id bibendum diam. In eu ante tellus.</p>",

    "<p>In mollis tempor fermentum. Vivamus non pulvinar nibh. Nullam laoreet, sapien sagittis vestibulum mollis, felis elit semper ex, eu sollicitudin quam justo nec nisl. Sed at tristique ante, a porta neque. In vel sem dolor. Nunc sed dui porta, dictum ante sed, dictum metus.</p>",

    "<p>Morbi sollicitudin velit magna, vel vestibulum justo pretium non. Pellentesque ultricies metus ac odio tincidunt, quis volutpat nulla laoreet. Sed felis elit, iaculis eu fermentum quis, accumsan non dui. Phasellus id laoreet odio, condimentum congue turpis.</p>",

    "<p>Sed condimentum dui sollicitudin tellus vulputate elementum. Curabitur et ex suscipit, pellentesque justo et, maximus turpis. Vivamus maximus sit amet nunc ac porta. Vestibulum molestie cursus iaculis. Suspendisse orci nisi, sagittis at ex suscipit, mattis gravida libero.</p>",

    "<p>Suspendisse consequat, leo ullamcorper ultricies volutpat, lectus nibh pellentesque leo, non consequat eros massa eu enim. Donec malesuada elementum turpis, ut blandit urna sagittis eu. Aliquam tincidunt quis augue ac sagittis.</p>",

    "<p>Aenean aliquam bibendum sodales. Duis et magna interdum, interdum eros condimentum, vulputate elit. In pretium risus eros, ac dignissim risus luctus ac. Duis gravida quis metus sed eleifend.</p>",

    "<p>Morbi sagittis tortor eget aliquet lobortis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse accumsan lacinia urna quis bibendum.</p>",

    "<p>Phasellus auctor turpis quis erat venenatis, in euismod mauris congue. Morbi porta nulla ut consectetur iaculis. In lacinia sodales magna sed scelerisque. Ut commodo eget augue eget lobortis. Vestibulum dignissim mi et eros tristique, non consectetur leo laoreet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam porta congue felis at malesuada.</p>",

    "<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam ultrices, arcu et lobortis consectetur, dolor ipsum varius diam, sit amet ornare nisi risus a neque. Duis id dui in nisl posuere faucibus. Etiam et turpis ac eros finibus feugiat.</p>",
]

CATEGORIES = [
    {
        "name": "Pro Categorie A",
        "title": "Pro Categorie A (H1)",
        "target": "PROFESSIONNEL",
        "headline": "HEADLINE / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "body1": "<h2>test</h2>"
    },
    {
        "name": "Pro Categorie B",
        "title": "Pro Categorie B (H1)",
        "target": "PROFESSIONNEL",
        "headline": "HEADLINE / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "body1": "<h2>test</h2>"
    },
    {
        "name": "Pro Categorie C",
        "title": "Pro Categorie C (H1)",
        "target": "PROFESSIONNEL",
        "headline": "HEADLINE / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "body1": "<h2>test</h2>"
    },
    {
        "name": "Aide à domicile",
        "title": "Aide à domicile",
        "target": "PARTICULIER",
        "headline": "...???...",
        "body1": "<h2>...???...</h2>"
    },
    {
        "name": "Part. Categorie B",
        "title": "Part. Categorie B (H1)",
        "target": "PARTICULIER",
        "headline": "HEADLINE / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "body1": "<h2>test</h2>"
    },
    {
        "name": "Part. Categorie C",
        "title": "Part. Categorie C (H1)",
        "target": "PARTICULIER",
        "headline": "HEADLINE / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "body1": "<h2>test</h2>"
    },
]

SERVICES = [
    {
        "name": "Service pour pro #1",
        "category": "Pro Categorie A",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour pro #2",
        "category": "Pro Categorie A",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour pro #3",
        "category": "Pro Categorie A",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour pro #4",
        "category": "Pro Categorie B",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour pro #5",
        "category": "Pro Categorie B",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour pro #6",
        "category": "Pro Categorie C",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour pro #7",
        "category": "Pro Categorie C",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour pro #8",
        "category": "Pro Categorie C",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Entretien du domicile",
        "category": "Aide à domicile",
        "available": True,
        "description": """Vous avez besoin d’aide dans vos tâches quotidiennes, que ce soit de façon régulière ou ponctuelle ?  Nous mettons à votre disposition des services de ménage et de nettoyage de vitres (jusqu’à 2,50 m), terrasse ou balcon.
        Les salariés sont formés tout au long de l’année par notre équipe de permanents et un plan de formations dédié.""",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Repassage",
        "category": "Aide à domicile",
        "available": True,
        "description": """Fer à repasser ou centrale vapeur, confiez votre linge à nos salariés expérimentés et formés. Nous analyserons avec vous vos besoins et mettrons à disposition la personne adéquate.
        Les salariés sont formés tout au long de l’année par notre équipe de permanents et un plan de formations dédié.""",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Préparation de repas à domicile",
        "category": "Aide à domicile",
        "available": True,
        "description": """Vous manquez de temps  ou avez un problème de santé qui vous empêche de cuisiner ? Abeilles Aide et Entraide met à votre disposition un de ses salariés pour vous préparer des repas selon vos habitudes. Nous nous adaptons à vos envies et pouvons vous faire découvrir des saveurs inédites.""",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour part. #3",
        "category": "Part. Categorie B",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour part. #4",
        "category": "Part. Categorie B",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour part. #5",
        "category": "Part. Categorie B",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour part. #6",
        "category": "Part. Categorie C",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour part. #7",
        "category": "Part. Categorie C",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
    {
        "name": "Service pour part. #8",
        "category": "Part. Categorie C",
        "available": True,
        "description": "DESCRIPTION / Suspendisse urna nunc, posuere id risus vitae, aliquet lobortis lectus. Morbi id consequat metus. Quisque eget ligula dui. Aliquam sem orci, volutpat ut tempor ut, ultricies sit amet velit.",
        "amplitude": "(amplitude)",
        "location": "location",
        "date": "2021-07-23"
    },
]

HOMEPAGE = {

    "presentation": """
<p>Elle accueille, accompagne et propose du travail durable &agrave; des personnes priv&eacute;es d&rsquo;emploi.</p>
<p>Elle participe &agrave; la coh&eacute;sion sociale et au d&eacute;veloppement &eacute;conomique du territoire Val d&rsquo;Yerres - Val de Seine (Essonne).</p>
<p>Cr&eacute;&eacute;e il y a plus de 30 ans, elle est agr&eacute;&eacute;e par l&rsquo;&Eacute;tat.</p>
    """,

    "services_presentation": "Des professionnels qui proposent de nombreux services",

    "garden_presentation": """<p>Espace d’agriculture périurbaine unique
sur le territoire, le jardin produit à Crosne 130 variétés de légumes bio et de saison et des œufs extra frais.</p>
<p>Paniers hebdomadaires proposés sur abonnement, à venir chercher sur place.</p>""",

    "benefit1_title": "Un ancrage local, une efficacité maximale",
    "benefit1": "Le partenariat de proximit&eacute; d&eacute;velopp&eacute; avec tous les acteurs de l&rsquo;emploi vous garantit efficacit&eacute; et rapidit&eacute; dans nos interventions.",
    "benefit2_title": "Une structure à dimension humaine, des services sur mesure",
    "benefit2": "Pour chaque mission, un référent dédié qui connaît le dossier et intervient en cas de problème.",
    "benefit3_title": "Une équipe qualifiée, des recrutements facilités",
    "benefit3": "Un suivi technique sur site, un interlocuteur unique, un accompagnement personnalisé pour chaque salarié.",
    "benefit4_title": "Un acteur de la transition écologique",
    "benefit4": "Nous nous engageons en faveur de la biodiversité et pour la promotion de pratiques respectueuses de l’environnement.",

    "meta_title": "META TITLE homepage",
    "meta_description": "META DESCRIPTION homepage",
}

PAGE_GARDEN = {
    "title": "Page Jardin",
    "headline": "(page jardin) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    # "image1": "default.webp",
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "jardin",
}

PAGE_GARDEN_PROJECT = {
    "title": "Page Jardin - projet",
    "headline": "(page jardin projet) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    # "image1": "default.webp",
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "jardin-project",
}

PAGE_BASKET = {
    "title": "Page Panier",
    "headline": "(page panier) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    # "image1": "default.webp",
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "panier",
}

PAGE_ASSOCIATION = {
    "title": "Page Association",
    "headline": "(page association) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "association",
}

PAGE_TEAM = {
    "title": "Page Equipe",
    "headline": "(page équipe) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "equipe",
}

PAGE_MISSIONS = {
    "title": "Page Missions",
    "headline": "(page Missions) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "nos-missions",
}

# PAGE_VALUES = {
#     "title": "Page valeurs",
#     "headline": "(page valeurs) " + random.choice(LOREM_IPSUM)[:25] + "...",
#     "body1": "(1) " + random.choice(LOREM_IPSUM),
#     "body2": "(2) " + random.choice(LOREM_IPSUM),
#     "body3": "(3) " + random.choice(LOREM_IPSUM), 
#     "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
#     "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
#     "slug": "nos-valeurs",
# }


# PAGE_PARTNERS = {
#     "title": "Page partenaires",
#     "headline": "(page partenaires) " + random.choice(LOREM_IPSUM)[:25] + "...",
#     "body1": "(1) " + random.choice(LOREM_IPSUM),
#     "body2": "(2) " + random.choice(LOREM_IPSUM),
#     "body3": "(3) " + random.choice(LOREM_IPSUM), 
#     "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
#     "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
#     "slug": "nos-partenaires",
# }

PAGE_TERRITORIAL_INFLUENCE = {
    "title": "Page Rayonnement territorial",
    "headline": "(Page Rayonnement territorial) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "rayonnementrterritorial",
}

PAGE_JOBHUNT = {
    "title": "Demandeurs d'emploi",
    "headline": "(emploi) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "emploi",
}

PAGE_SERVICES = {
    "title": "Services",
    "headline": "(services) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "services",
}

PAGE_SERVICES_PRO = {
    "title": "Services pour professionnels",
    "headline": "(services pro) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "<h2>Responsabilité sociétale</h2>" + random.choice(LOREM_IPSUM),
    "body3": "<h2>Ils nous font confiance</h2>", 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "services-pour-professionnels",
}

PAGE_SERVICES_IND = {
    "title": "Services pour particuliers",
    "headline": "(services ind) " + random.choice(LOREM_IPSUM)[:25] + "...",
    "body1": "(1) " + random.choice(LOREM_IPSUM),
    "body2": "(2) " + random.choice(LOREM_IPSUM),
    "body3": "(3) " + random.choice(LOREM_IPSUM), 
    "meta_title": "m_title: " + random.choice(LOREM_IPSUM)[:10],
    "meta_description": "meta_desc:" + random.choice(LOREM_IPSUM)[:10],
    "slug": "services-pour-particuliers",
}

POSTS = [
    {
        "category": "NEWS",
        "promoted": True,
        "title": "POST_NEWS_1",
        "extract": "post_news_1" + random.choice(LOREM_IPSUM)[:25] + "...",
        "body": random.choice(LOREM_IPSUM),
    },
    {
        "category": "NEWS",
        "promoted": True,
        "title": "POST_NEWS_2",
        "extract": "post_news_2" + random.choice(LOREM_IPSUM)[:25] + "...",
        "body": random.choice(LOREM_IPSUM),
    },
    {
        "category": "NEWS",
        "promoted": True,
        "title": "POST_NEWS_3",
        "extract": "post_news_3" + random.choice(LOREM_IPSUM)[:25] + "...",
        "body": random.choice(LOREM_IPSUM),
    },
    {
        "category": "GARDEN",
        "promoted": True,
        "title": "POST_GARDEN_1",
        "extract": "post_GARDEN_1" + random.choice(LOREM_IPSUM)[:25] + "...",
        "body": random.choice(LOREM_IPSUM),
    },
    {
        "category": "GARDEN",
        "promoted": True,
        "title": "POST_GARDEN_2",
        "extract": "post_GARDEN_2" + random.choice(LOREM_IPSUM)[:25] + "...",
        "body": random.choice(LOREM_IPSUM),
    },
    {
        "category": "GARDEN",
        "promoted": True,
        "title": "POST_GARDEN_3",
        "extract": "post_GARDEN_3" + random.choice(LOREM_IPSUM)[:25] + "...",
        "body": random.choice(LOREM_IPSUM),
    },
]

USERS = [
    {
        "username": "gil",
        "email": "gil@me.net",
    },
    {
        "username": "adrien",
        "email": "adrien@me.net",
    },
    {
        "username": "paul",
        "email": "paul@me.net",
    },
    {
        "username": "abeilles",
        "email": "abeilles@me.net",
    },
]


class ServiceCleaner:
    def __init__(self):
        pass
    def reset_categories(self):
        Category.objects.all().delete()
        Service.objects.all().delete()
    def create_categories(self):
        for category in CATEGORIES:
            new_category = Category()
            new_category.weight = 1
            new_category.name = category["name"]
            new_category.target = category["target"]
            new_category.title = category["title"]
            new_category.headline = category["headline"]
            new_category.featured_image = "default.webp"
            new_category.body1 = category["body1"]
            new_category.image1 = "default.webp"
            new_category.save()
    def create_services(self):
        for service in SERVICES:
            new_service = Service()
            new_service.name = service["name"]
            new_service.category = Category.objects.get(name=service["category"])
            new_service.available = service["available"]
            new_service.description = service["description"]
            new_service.amplitude = service["amplitude"]
            new_service.location = service["location"]
            new_service.date = service["date"]
            new_service.save()


class PageCleaner:
    def __init__(self):
        pass
    def create_pages_helper(self, new_page, data, testimonials=False, page_type=""):
        new_page.title = data["title"]
        new_page.headline = data["headline"]
        if data is not PAGE_JOBHUNT:
            new_page.featured_image = "default.webp"
        new_page.body1 = data["body1"]
        if data is not PAGE_BASKET and data is not PAGE_GARDEN:
            new_page.image1 = "default.webp"
        if data is not PAGE_SERVICES_IND:
            new_page.body2 = data["body2"]
        if data is not PAGE_BASKET and \
            data is not PAGE_SERVICES_IND and \
            data is not PAGE_SERVICES_PRO:
            new_page.image2 = "default.webp"
        if data is not PAGE_SERVICES_IND:
            new_page.body3 = data["body3"]
        if data is not PAGE_BASKET and data is not PAGE_SERVICES_IND:
            new_page.image3 = "default.webp"
        new_page.meta_title = data["meta_title"]
        new_page.meta_description = data["meta_description"]

        if testimonials:
            new_page.testimony_title = "Témoignages (titre)"
            new_page.testimony1_image = "default_square.webp"
            new_page.testimony1_name = "Client #1"
            new_page.testimony1_text = random.choice(LOREM_IPSUM)[:80]
            new_page.testimony2_image = "default_square.webp"
            new_page.testimony2_name = "Client #2"
            new_page.testimony2_text = random.choice(LOREM_IPSUM)[:80]
            new_page.testimony3_image = "default_square.webp"
            new_page.testimony3_name = "Client #3"
            new_page.testimony3_text = random.choice(LOREM_IPSUM)[:80]

        if page_type == 'PAGE_JOBHUNT':
            new_page.body_extra = "Comment postuler | " + random.choice(LOREM_IPSUM)[:80]
            new_page.image_extra = "default.webp"

        if page_type == 'PAGE_BASKET':
            new_page.body_extra = "<p>Nous proposons également les légumes à la vente directe <strong>le mercredi de 15 h à 19 h</strong></p>"
            new_page.body_food = """
<h2>Printemps</h2>
<ul>
    <li>Pomme de terre primeur</li>
    <li>Carotte primeur</li>
    <li>Petit-pois</li>
    <li>Pois-Mangetout</li>
    <li>Fève</li>
    <li>Épinard</li>
    <li>Betterave</li>
    <li>Blette</li>
    <li>Chou-chinois</li>
    <li>Chou (brocoli</li>
    <li>fleurs...)</li>
    <li>Fenouil</li>
    <li>Radis</li>
    <li>Oignon blanc</li>
    <li>Laitue</li>
    <li>Roquette</li>
    <li>Coriandre</li>
    <li>Aneth</li>
    <li>Fraise</li>
    <li>Framboise</li>
    <li>Cardon</li>
    <li>Navet</li>
    <li>Ciboulette</li>
    <li>Pimprenelle</li>
    <li>Thym</li>
    <li>Sauge</li>
    <li>Feuille de Pissenlit</li>
</ul>
<h2>Été</h2>
<ul>
    <li>Aubergine</li>
    <li>Poivron</li>
    <li>Piment</li>
    <li>Laitue et Chicorée</li>
    <li>Tomate</li>
    <li>Concombre et Cornichon</li>
    <li>Courgette</li>
    <li>Pâtisson</li>
    <li>Haricot</li>
    <li>Fenouil</li>
    <li>Melon</li>
    <li>Échalote</li>
    <li>Pois-cassé</li>
    <li>Ail</li>
    <li>Persil</li>
    <li>Menthe</li>
    <li>Basilic</li>
    <li>Fraise</li>
    <li>Framboise</li>
    <li>Groseille</li>
    <li>Artichaut</li>
</ul>
<h2>Automne</h2>
<ul>
    <li>Courge</li>
    <li>Navet</li>
    <li>Pomme de terre</li>
    <li>Laitue et Chicorée</li>
    <li>Haricot sec</li>
    <li>Chou-chinois</li>
    <li>Panais</li>
    <li>Persil tubéreux</li>
    <li>Blette</li>
    <li>Épinard</li>
    <li>Rutabaga</li>
    <li>Céleri-rave et branche</li>
    <li>Oignon</li>
    <li>Chou-rave</li>
    <li>Chou (Rouge, Cabus, vert...)</li>
    <li>Fenouil</li>
    <li>Radis</li>
    <li>Patate douce</li>
    <li>Cresson</li>
    <li>Maïs</li>
    <li>Graines de Tournesol</li>
</ul>
<h2>Hiver</h2>
<ul>
    <li>Épinard</li>
    <li>Radis noir</li>
    <li>Mâche</li>
    <li>Poireau</li>
    <li>Pomme de terre</li>
    <li>Courge et Potimarron</li>
    <li>Panais</li>
    <li>Carotte</li>
    <li>Oignon</li>
    <li>Ail</li>
    <li>Betterave</li>
    <li>Chou (de Bruxelles, cabus...)</li>
    <li>Navet</li>
    <li>Céleri</li>
    <li>Topinambour</li>
    <li>Hélianti</li>
    <li>Choux</li>
    <li>Crosne</li>
    <li>Salsifis</li>
    <li>Scorsonère</li>
    <li>Verveine</li>
</ul>"""
            # new_page.body3 = data["body3"]

        new_page.save()

    def clean_homepage(self):
        Homepage.objects.all().delete()

    def create_homepage(self):
        new_homepage = Homepage()
        new_homepage.presentation = HOMEPAGE["presentation"]
        new_homepage.services_presentation = HOMEPAGE["services_presentation"]
        new_homepage.garden_presentation = HOMEPAGE["garden_presentation"]
        new_homepage.garden_image = "default.webp"
        new_homepage.benefit1_title = HOMEPAGE["benefit1_title"]
        new_homepage.benefit1 = HOMEPAGE["benefit1"]
        new_homepage.benefit2_title = HOMEPAGE["benefit2_title"]
        new_homepage.benefit2 = HOMEPAGE["benefit2"]
        new_homepage.benefit3_title = HOMEPAGE["benefit3_title"]
        new_homepage.benefit3 = HOMEPAGE["benefit3"]
        new_homepage.benefit4_title = HOMEPAGE["benefit4_title"]
        new_homepage.benefit4 = HOMEPAGE["benefit4"]
        new_homepage.meta_title = HOMEPAGE["meta_title"]
        new_homepage.meta_description = HOMEPAGE["meta_description"]
        new_homepage.save()
    
    def create_pages(self):

        # AA&E

        PageAssociation.objects.all().delete()
        new_page = PageAssociation()
        self.create_pages_helper(new_page, PAGE_ASSOCIATION)

        # PageTeam.objects.all().delete()
        # new_page = PageTeam()
        # self.create_pages_helper(new_page, PAGE_TEAM)

        PageMissions.objects.all().delete()
        new_page = PageMissions()
        self.create_pages_helper(new_page, PAGE_MISSIONS)

        # PageValues.objects.all().delete()
        # new_page = PageValues()
        # self.create_pages_helper(new_page, PAGE_VALUES)

        # PagePartners.objects.all().delete()
        # new_page = PagePartners()
        # self.create_pages_helper(new_page, PAGE_PARTNERS)

        PageTerritorialInfluence.objects.all().delete()
        new_page = PageTerritorialInfluence()
        self.create_pages_helper(new_page, PAGE_TERRITORIAL_INFLUENCE)

        # Garden

        PageGarden.objects.all().delete()
        new_page = PageGarden()
        new_page.benefit1_title = HOMEPAGE["benefit1_title"]
        new_page.benefit1 = HOMEPAGE["benefit1"]
        new_page.benefit2_title = HOMEPAGE["benefit2_title"]
        new_page.benefit2 = HOMEPAGE["benefit2"]
        new_page.benefit3_title = HOMEPAGE["benefit3_title"]
        new_page.benefit3 = HOMEPAGE["benefit3"]
        self.create_pages_helper(new_page, PAGE_GARDEN, testimonials=True)

        PageGardenProject.objects.all().delete()
        new_page = PageGardenProject()
        self.create_pages_helper(new_page, PAGE_GARDEN_PROJECT)

        PageBasket.objects.all().delete()
        new_page = PageBasket()
        self.create_pages_helper(new_page, PAGE_BASKET, page_type="PAGE_BASKET")

        # Others

        PageJobhunt.objects.all().delete()
        new_page = PageJobhunt()
        self.create_pages_helper(new_page, PAGE_JOBHUNT, testimonials=True, page_type="PAGE_JOBHUNT")

        # PageServices.objects.all().delete()
        # new_page = PageServices()
        # self.create_pages_helper(new_page, PAGE_SERVICES, testimonials=True)

        PageServicesPro.objects.all().delete()
        new_page = PageServicesPro()
        self.create_pages_helper(new_page, PAGE_SERVICES_PRO, testimonials=True)

        PageServicesInd.objects.all().delete()
        new_page = PageServicesInd()
        self.create_pages_helper(new_page, PAGE_SERVICES_IND, testimonials=True)


class QuestionsCleaner:
    def __init__(self):
        pass
    def clean_questions(self):
        QuestionServicesPro.objects.all().delete()
        QuestionServicesInd.objects.all().delete()
        QuestionGarden.objects.all().delete()
    def create_questions(self):
        for q in range(1,9):
            new_question = QuestionGarden()
            new_question.question = f"{random.choice(LOREM_IPSUM)[:25]} ? ({q})"
            new_question.response = random.choice(LOREM_IPSUM)[:100] + "."
            new_question.weight = q
            new_question.save()
        for q in range(1,9):
            new_question = QuestionServicesInd()
            new_question.question = f"{random.choice(LOREM_IPSUM)[:25]} ? ({q})"
            new_question.response = random.choice(LOREM_IPSUM)[:100] + "."
            new_question.weight = q
            new_question.save()
        for q in range(1,9):
            new_question = QuestionServicesPro()
            new_question.question = f"{random.choice(LOREM_IPSUM)[:25]} ? ({q})"
            new_question.response = random.choice(LOREM_IPSUM)[:100] + "."
            new_question.weight = q
            new_question.save()


class PostsCleaner:
    def __init__(self):
        pass
    def clean_posts(self):
        Post.objects.all().delete()
    def create_posts(self):
        for post in POSTS:
            new_post = Post()
            new_post.category = post["category"]
            new_post.promoted = post["promoted"]
            new_post.title = post["title"]
            new_post.extract = post["extract"]
            new_post.body = post["body"]
            new_post.image = "default.webp"
            new_post.save()

    
class UsersCleaner:
    def __init__(self):
        pass
    def clean_users(self):
        User.objects.all().delete()
    def create_users(self):
        for user in USERS:
            new_user = User()
            new_user.username = user["username"]
            new_user.email = user["email"]
            new_user.set_password("pass")
            new_user.is_active = True
            new_user.is_staff = True
            new_user.is_superuser = True
            new_user.save()


class BasketCleaner:
    def __init__(self):
        pass
    def clean_basket(self):
        Basket.objects.all().delete()
    def create_basket(self):
        new_basket = Basket()
        new_basket.total = 100
        new_basket.booked = 85
        new_basket.save()


# class SettingsCleaner:
#     def __init__(self):
#         pass
#     def clean_settings(self):
#         ContactEmail.objects.all().delete()
#         NewsletterConfig.objects.all().delete()
#         RecipientEmail.objects.all().delete()
#         SocialLinks.objects.all().delete()
#     def create_settings(self):
#         pass

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Services
        service_cleaner = ServiceCleaner()
        service_cleaner.reset_categories()
        service_cleaner.create_categories()
        service_cleaner.create_services()
        # Pages
        page_cleaner = PageCleaner()
        page_cleaner.clean_homepage()
        page_cleaner.create_homepage()
        page_cleaner.create_pages()
        # Posts
        posts_cleaner = PostsCleaner()
        posts_cleaner.clean_posts()
        posts_cleaner.create_posts()
        # Users
        user_cleaner = UsersCleaner()
        user_cleaner.clean_users()
        user_cleaner.create_users()
        # Basket
        basket_cleaner = BasketCleaner()
        basket_cleaner.clean_basket()
        basket_cleaner.create_basket()
        # Questions
        questions_cleaner = QuestionsCleaner()
        questions_cleaner.clean_questions()
        questions_cleaner.create_questions()


# partenaires, equipe => qui sommes nous 

# Missions valeurs engagement

# Rayonnement territorial => TOUT NOUVEAU

# Actus 