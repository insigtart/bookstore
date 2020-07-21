from django.db import models

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

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    datetime = models.DateField()
    country = models.ManyToManyField(Country)
    languages = models.ManyToManyField(Language)
    topics = models.ManyToManyField(Topic)