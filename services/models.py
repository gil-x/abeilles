from django.db import models
from django.forms import widgets
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

SERVICE_FOR = (
        ("PARTICULIER", "Particulier"),
        ("PROFESSIONNEL", "Professionnel"),
    )

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Nom", blank=True)
    target = models.CharField(
            max_length=13, choices=SERVICE_FOR,
            default="PARTICULIER", verbose_name=u"Service pour *"
        )
    weight = models.IntegerField(verbose_name="Poids de la catégorie", default=1)
    title = models.CharField(max_length=50, verbose_name=u"Titre H1 de la page")
    headline = models.TextField(null=True, blank=True, verbose_name=u"Chapeau (H2)")
    featured_image = models.ImageField(blank=True, verbose_name=u"Image en une")
    body1 = RichTextField(null=True, blank=True, verbose_name=u"Bloc de texte #1")
    image1 = models.ImageField(blank=True, verbose_name=u"Image optionnelle #1")

    meta_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"META title")
    meta_description = models.CharField(max_length=140, null=True, blank=True, verbose_name=u"META description")
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Catégories"

    def save(self, *args, **kwargs):
        """
        If slug already exists and object is brand new,
        then add a '-' and an integer, which garantees unique slug.
        """
        SLUG = slugify(self.title)
        slug_candidate = SLUG
        increment = 0
        while Category.objects.filter(slug=slug_candidate) and not self.id:
            increment += 1
            slug_candidate = f"{SLUG}-{increment}"
        self.slug = slug_candidate
        super(Category, self).save(*args, **kwargs)
        

class Service(models.Model):

    name = models.CharField(max_length=50, verbose_name=u"Nom", blank=True)
    # target = models.CharField(
    #         max_length=13, choices=SERVICE_FOR,
    #         default="PARTICULIER", verbose_name=u"Service pour *"
    #     )
    category = models.ForeignKey(
            Category, null=True, blank=True, verbose_name=u"Catégorie",
            on_delete=models.CASCADE)
    available = models.BooleanField(default=False, verbose_name=u"Disponible")
    
    description = models.TextField(verbose_name=u"Descriptif du poste *", blank=True)
    amplitude = models.CharField(max_length=50, verbose_name=u"Amplitude horaires *", null=True, blank=True)
    location = models.CharField(max_length=50, verbose_name=u"Lieu de travail *", blank=True)
    date = models.DateField(null=True, verbose_name=u"Date de dépôt", blank=True)

    slug = models.SlugField(null=True, blank=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        """
        If slug already exists and object is brand new,
        then add a '-' and an integer, which garantees unique slug.
        """
        SLUG = slugify(self.name)
        slug_candidate = SLUG
        increment = 0
        while Service.objects.filter(slug=slug_candidate) and not self.id:
            increment += 1
            slug_candidate = f"{SLUG}-{increment}"
        self.slug = slug_candidate
        super(Service, self).save(*args, **kwargs)

    # def services_list(self):
    #     # return [ (service.name, service.name) for service in Service.objects.all() ]
    #     return [ ("a", "a"), ("b", "b") ("c", "c"), ]