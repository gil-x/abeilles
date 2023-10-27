from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify

ROLE = (
        # ("HOMEPAGE", "Accueil"),
        ("GARDEN", "Jardin"),
        ("JOBHUNT", "Recherche d'emploi"),
        ("ASSOCIATION", "Association"),

        ("SERVICES", "Services"),
        ("SERVICES_PRO", "Services aux Professionnels"),
        ("SERVICES_IND", "Services Particuliers"),
    )


class Homepage(models.Model):
    presentation = RichTextField(null=True, blank=True, verbose_name=u"Présentation générale")
    services_presentation = RichTextField(null=True, blank=True, verbose_name=u"Présentation des services")
    garden_presentation = RichTextField(null=True, blank=True, verbose_name=u"Présentation du jardin")
    garden_image = models.ImageField(blank=True, verbose_name=u"Photo du jardin")
    benefit1_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 1")
    benefit1 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 1")
    benefit2_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 2")
    benefit2 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 2")
    benefit3_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 3")
    benefit3 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 3")
    benefit4_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 4")
    benefit4 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 4")

    meta_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"META title")
    meta_description = models.CharField(max_length=140, null=True, blank=True, verbose_name=u"META description")

    def __str__(self):
        return "Accueil"
    
    class Meta:
        verbose_name = 'Accueil'
        verbose_name_plural = '  Accueil'


class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"Titre")
    headline = models.TextField(null=True, blank=True, verbose_name=u"Chapeau (H2)")
    featured_image = models.ImageField(blank=True, verbose_name=u"Image en une")

    body1 = RichTextUploadingField(null=True, blank=True, verbose_name=u"Bloc de texte #1")
    image1 = models.ImageField(blank=True, verbose_name=u"Image optionnelle #1")
    body2 = RichTextUploadingField(null=True, blank=True, verbose_name=u"Bloc de texte #2")
    image2 = models.ImageField(blank=True, verbose_name=u"Image optionnelle #2")
    body3 = RichTextUploadingField(null=True, blank=True, verbose_name=u"Bloc de texte #3")
    image3 = models.ImageField(blank=True, verbose_name=u"Image optionnelle #3")

    meta_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"META title")
    meta_description = models.CharField(max_length=140, null=True, blank=True, verbose_name=u"META description")
    # slug = models.SlugField(null=True, blank=True)
    class Meta:
        abstract = True


class PageWithTestimonials(models.Model):
    testimony_title = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"Titre de la section")
    testimony1_image = models.ImageField(blank=True, verbose_name=u"Photo du client #1")
    testimony1_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"Nom du client #1")
    testimony1_text = models.CharField(max_length=512, null=True, blank=True, verbose_name=u"Témoignage #1")
    testimony2_image = models.ImageField(blank=True, verbose_name=u"Photo du client #2")
    testimony2_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"Nom du client #2")
    testimony2_text = models.CharField(max_length=512, null=True, blank=True, verbose_name=u"Témoignage #2")
    testimony3_image = models.ImageField(blank=True, verbose_name=u"Photo du client #3")
    testimony3_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=u"Nom du client #3")
    testimony3_text = models.CharField(max_length=512, null=True, blank=True, verbose_name=u"Témoignage #3")
    class Meta:
        abstract = True


class PageAssociation(Page):
    def __str__(self):
        return f"Page Qui somme-nous"
    class Meta:
        verbose_name = 'Qui somme-nous'
        verbose_name_plural = ' AAE - Qui somme-nous'


# class PageTeam(Page):
#     def __str__(self):
#         return f"Page de l\'équipe"
#     class Meta:
#         verbose_name = 'Équipe'
#         verbose_name_plural = 'AAE - Équipe'


class PageMissions(Page):
    def __str__(self):
        return f"Page des Missions, Valeurs, Engagement"
    class Meta:
        verbose_name = 'Missions, Valeurs, Engagement'
        verbose_name_plural = 'AAE - Missions, Valeurs, Engagement'




class PageTerritorialInfluence(Page):
    def __str__(self):
        return f"Page du Rayonnement territorial"
    class Meta:
        verbose_name = 'Rayonnement territorial'
        verbose_name_plural = 'AAE - Rayonnement territorial'
 
# class PageValues(Page):
#     def __str__(self):
#         return f"Page de nos valeurs"
#     class Meta:
#         verbose_name = 'Nos valeurs'
#         verbose_name_plural = 'AAE - Nos valeurs'


# class PagePartners(Page):
#     def __str__(self):
#         return f"Page de nos partenaires"
#     class Meta:
#         verbose_name = 'Nos partenaires'
#         verbose_name_plural = 'AAE - Nos partenaires'


class PageGarden(Page, PageWithTestimonials):
    benefit1_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 1")
    benefit1 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 1")
    benefit2_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 2")
    benefit2 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 2")
    benefit3_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 3")
    benefit3 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 3")
    # benefit4_title = models.TextField(null=True, blank=True, verbose_name=u"Titre Avantage 4")
    # benefit4 = RichTextField(null=True, blank=True, verbose_name=u"Avantage 4")
    def __str__(self):
        return f"Page du jardin"
    class Meta:
        verbose_name = 'Jardin'
        verbose_name_plural = 'Jardin'


class PageGardenProject(Page):
    def __str__(self):
        return f"Page du jardin - le projet"
    class Meta:
        verbose_name = 'Jardin - le projet'
        verbose_name_plural = 'Jardin - le projet'


class PageBasket(Page):
    body_extra = RichTextField(null=True, blank=True, verbose_name=u"Bloc de texte `Vente directe`")
    body_food = RichTextField(null=True, blank=True, verbose_name=u"Bloc de texte `fruits et légumes`")
    def __str__(self):
        return f"Page du jardin - paniers"
    class Meta:
        verbose_name = 'Jardin - paniers'
        verbose_name_plural = 'Jardin - paniers'



class PageJobhunt(Page, PageWithTestimonials):
    body_extra = RichTextUploadingField(null=True, blank=True, verbose_name=u"Bloc de texte `Comment postuler ?`")
    image_extra = models.ImageField(blank=True, verbose_name=u"Image `Comment postuler ?`")
    def __str__(self):
        return f"Page pour les demandeurs d\'emploi"
    class Meta:
        verbose_name = 'Demandeurs d\'emploi'
        verbose_name_plural = 'Demandeurs d\'emploi'


class PageServices(Page, PageWithTestimonials):
    def __str__(self):
        return f"Page des services"
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'


class PageServicesPro(Page, PageWithTestimonials):
    def __str__(self):
        return f"Page des services pour professionnels"
    class Meta:
        verbose_name = 'Services pour professionnels'
        verbose_name_plural = 'Services pour professionnels'


class PageServicesInd(Page, PageWithTestimonials):
    def __str__(self):
        return f"Page des services pour particuliers"
    class Meta:
        verbose_name = 'Services pour particuliers'
        verbose_name_plural = 'Services pour particuliers'


class PageCustom(models.Model):
    role = models.CharField(
            max_length=20,
            choices=ROLE,
            verbose_name=u"Role",
        )
    title = models.CharField(max_length=50, verbose_name=u"Titre")
    headline = models.TextField(null=True, blank=True, verbose_name=u"Chapeau (H2)")
    featured_image = models.ImageField(blank=True, verbose_name=u"Image en une")

    body1 = RichTextField(null=True, blank=True, verbose_name=u"Bloc de texte #1")
    image1 = models.ImageField(blank=True, verbose_name=u"Image optionnelle #1")
    body2 = RichTextField(null=True, blank=True, verbose_name=u"Bloc de texte #2")
    image2 = models.ImageField(blank=True, verbose_name=u"Image optionnelle #2")
    body3 = RichTextField(null=True, blank=True, verbose_name=u"Bloc de texte #3")
    image3 = models.ImageField(blank=True, verbose_name=u"Image optionnelle #3")

    meta_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"META title")
    meta_description = models.CharField(max_length=140, null=True, blank=True, verbose_name=u"META description")
    slug = models.SlugField(null=True, blank=True)
 
    def __str__(self):
        return f"{self.title} ({self.role.lower()})"
    
    class Meta:
        ordering = ['role', 'title']

    def save(self, *args, **kwargs):
        """
        If slug already exists and object is brand new,
        then add a '-' and an integer, which garantees unique slug.
        """
        SLUG = slugify(self.title)
        slug_candidate = SLUG
        increment = 0
        while Page.objects.filter(slug=slug_candidate) and not self.id:
            increment += 1
            slug_candidate = f"{SLUG}-{increment}"
        self.slug = slug_candidate
        super(Page, self).save(*args, **kwargs)