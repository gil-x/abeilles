from django.db import models


class ContactEmail(models.Model):
    email = models.EmailField(
            max_length=50,
            default="contact@abeilles-aide-entraide.fr",
            verbose_name=u"Email d'expéditeur",
        )
    password = models.CharField(
            max_length=50, null=True, blank=True,
            verbose_name=u"Mot de passe de la messagerie",
        )
    port = models.IntegerField(default=1025)

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name_plural = "Email de contact"


class NewsletterConfig(models.Model):
    sendingblue_api_key = models.CharField(
        null=True, blank=True, max_length=255, verbose_name=u"Clé API")
    sendingblue_smtp_key = models.CharField(
        null=True, blank=True, max_length=50, verbose_name=u"Clé SMTP")

    def __str__(self):
        return f"Sendingblue"
    
    class Meta:
        verbose_name_plural = "Réglage Newsletter"


class RecipientEmail(models.Model):
    email = models.EmailField(
            max_length=50, null=True, blank=True,
            verbose_name=u"Email de réception",
        )
        
    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name_plural = "Email de réception"


class SocialLinks(models.Model):
    facebook = models.CharField(max_length=50, verbose_name=u"Page Facebook", default="#")
    instagram = models.CharField(max_length=50, verbose_name=u"Page Instagram", default="#")
    twitter = models.CharField(max_length=50, verbose_name=u"Page Twitter", default="#")
    linkedin = models.CharField(max_length=50, verbose_name=u"Page Linkedin", default="#")

    def __str__(self):
        return f"Réseaux sociaux"
    
    class Meta:
        verbose_name_plural = "Réseaux sociaux"
