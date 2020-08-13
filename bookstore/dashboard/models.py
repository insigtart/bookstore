from django.db import models
from django.urls import reverse

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name


class Notification(models.Model):
    target = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=64)
    datetime = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)


class Book(models.Model):
    title = models.CharField(max_length=256, verbose_name="Titlu")
    author = models.CharField(max_length=64, verbose_name="Autor")
    description = models.TextField(blank=False, verbose_name="Detalii")
    datetime = models.DateField(verbose_name="Data publicării")
    tracking = models.BooleanField(
        verbose_name="Status carte", null=True, default=False)
    country = models.ManyToManyField(Country, verbose_name="Țări")
    languages = models.ManyToManyField(Language, verbose_name="Limbi")
    topics = models.ManyToManyField(Topic, verbose_name="Categorii")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
