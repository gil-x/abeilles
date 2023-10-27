import os
from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


# CATEGORY = (
#         ("NEWS", "Actualité"),
#         ("GARDEN", "Jardin"),
#     )

CATEGORY_TRANSLATOR = {
        "NEWS": "Actualité",
        "TESTIMONY": "Témoignage",
        "GARDEN": "Jardin",
    }

class Post(models.Model):
    # category = models.CharField(max_length=9,
    #         choices=CATEGORY,
    #         default="NEWS", verbose_name=u"Catégorie",
    #     )
    promoted = models.BooleanField(
            default=False,
            verbose_name=u"Promu en page d'accueil"
        )

    title = models.CharField(max_length=60, verbose_name=u"Titre")
    extract = models.TextField(null=True, blank=True, verbose_name=u"Chapeau (H2)")
    body = RichTextField(null=True, blank=True, verbose_name=u"Corps")
    image = models.ImageField(null=True, blank=True,
            verbose_name=u"Image de l'article",
            upload_to="posts/",
        )
    file1 = models.FileField(null=True, blank=True,
            verbose_name=u"Fichier #1 à télécharger",
            upload_to="uploads/",
        )
    file1_name = models.CharField(
        null=True, blank=True,
        max_length=60, verbose_name=u"Nom du lien du Fichier #1")
    file2 = models.FileField(null=True, blank=True,
            verbose_name=u"Fichier #2 à télécharger",
            upload_to="uploads/",
        )
    file2_name = models.CharField(
        null=True, blank=True,
        max_length=60, verbose_name=u"Nom du lien du Fichier #2")

    meta_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"META title")
    meta_description = models.CharField(max_length=140, null=True, blank=True, verbose_name=u"META description")

    slug = models.SlugField(null=True, blank=True)

    created_at = models.DateTimeField(
            null=True, auto_now_add=True,
            verbose_name=u"Date de création",
        )
    updated_at = models.DateTimeField(
            null=True, auto_now=True,
            verbose_name=u"Dernière mise à jour",
        )
    
    def __str__(self):
        promoted = "(Promu en page d'accueil)" if self.promoted else ""
        # return f"{CATEGORY_TRANSLATOR[self.category]} - {self.title} { promoted }"
        return f"{self.title} { promoted }"

    class Meta:
        verbose_name_plural = "Articles"

    def save(self, *args, **kwargs):
        """
        If slug already exists and object is brand new,
        then add a '-' and an integer, which garantees unique slug.
        """
        SLUG = slugify(self.title)
        slug_candidate = SLUG
        increment = 0
        while Post.objects.filter(slug=slug_candidate) and not self.id:
            increment += 1
            slug_candidate = f"{SLUG}-{increment}"
        self.slug = slug_candidate
        super(Post, self).save(*args, **kwargs)

# class Category(models.Model):
#     category_name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.category_name

#     class Meta:
#         verbose_name_plural = "Catégories"

# class Position(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     rank = models.IntegerField()