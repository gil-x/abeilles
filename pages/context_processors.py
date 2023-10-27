from .forms import ContactForm
from basket.forms import NewsletterForm, BasketDemandForm
from services.models import Category
from pages.models import Homepage, PageGarden
from settings.models import SocialLinks

def webforms(request):
    return {
        "contact_form": ContactForm,
        "newsletter_form": NewsletterForm,
        "basket_form": BasketDemandForm,
    }

def menu_categories(request):
    return {
        "menu_categories_pro": Category.objects.filter(
            target="PROFESSIONNEL").order_by('-weight'),
        "menu_categories_ind": Category.objects.filter(
            target="PARTICULIER").order_by('-weight'),
    }

def benefits(request):
    homepage = Homepage.objects.first()
    return {
        "benefits": [
            {
                "title": homepage.benefit1_title,
                "text": homepage.benefit1,
            },
            {
                "title": homepage.benefit2_title,
                "text": homepage.benefit2,
            },
            {
                "title": homepage.benefit3_title,
                "text": homepage.benefit3,
            },
            {
                "title": homepage.benefit4_title,
                "text": homepage.benefit4,
            },
        ],
    }

def garden_benefits(request):
    garden_page = PageGarden.objects.first()
    return {
        "garden_benefits": [
            {
                "title": garden_page.benefit1_title,
                "text": garden_page.benefit1,
            },
            {
                "title": garden_page.benefit2_title,
                "text": garden_page.benefit2,
            },
            {
                "title": garden_page.benefit3_title,
                "text": garden_page.benefit3,
            },
        ],
    }


def social_links(request):
    links = SocialLinks.objects.first()
    return {
        "social_facebook": links.facebook if links else "#",
        "social_instagram": links.instagram if links else "#",
        "social_twitter": links.twitter if links else "#",
        "social_linkedin": links.linkedin if links else "#",
    }
