from django.db import models


class QuestionServicesPro(models.Model):
    question = models.CharField(max_length=255, verbose_name=u"Question *")
    response = models.TextField(verbose_name=u"Response *")
    weight = models.IntegerField()

    class Meta:
        ordering = ['weight', 'question']
        verbose_name = 'Services pro'
        verbose_name_plural = 'Services pro'

    def __str__(self):
        return f"{self.weight}) {self.question}"


class QuestionServicesInd(models.Model):
    question = models.CharField(max_length=255, verbose_name=u"Question *")
    response = models.TextField(verbose_name=u"Response *")
    weight = models.IntegerField()

    class Meta:
        ordering = ['weight', 'question']
        verbose_name = 'Services particuliers'
        verbose_name_plural = 'Services particuliers'

    def __str__(self):
        return f"{self.weight}) {self.question}"


class QuestionGarden(models.Model):
    question = models.CharField(max_length=255, verbose_name=u"Question *")
    response = models.TextField(verbose_name=u"Response *")
    weight = models.IntegerField()

    class Meta:
        ordering = ['weight', 'question']
        verbose_name = 'Questions pour le jardin'
        verbose_name_plural = 'Questions pour le jardin'

    def __str__(self):
        return f"{self.weight}) {self.question}"
