from typing import TextIO
from django.db import models

class Basket(models.Model):
    total = models.IntegerField(null=True, blank=True,
            verbose_name=u"Nombre total de paniers"
        )
    booked = models.IntegerField(null=True, blank=True,
            verbose_name=u"Nombre de paniers réservés"
        )

    def delta(self):
        return self.total - self.booked

    def delta_class(self):
        delta = self.total - self.booked
        if delta <= 0:
            return "soldout"
        elif delta < 5:
            return "last"
        elif delta < self.total / 4:
            return "critical"
        elif delta < self.total / 3:
            return "low"
        else:
            return "abondance"

    # def clean(self):
    #     model = self.__class__
    #     if (model.objects.count() > 0 and self.id != model.objects.get().id):
    #         raise ValidationError(
    #             "Can only create 1 instance of %s." % model.__name__)

    def __str__(self):
        return f"Panier"

    class Meta:
        verbose_name = 'Panier'
        verbose_name_plural = 'Panier'
