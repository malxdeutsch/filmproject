from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length = 200)

class Category(models.Model):
    name = models.CharField(max_length = 200)

class Film(models.Model):
    title = models.CharField(max_length = 200)
    release_date = models.DateField(default=timezone.now()),
    created_in_country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name = 'films_created_in')
    available_in_countries = models.ManyToManyField(Country, related_name = 'films_available_in')
    category = models.ManyToManyField(Category)
    director : models.ManyToManyField('Director')
    added_date = models.DateTimeField(auto_now_add=True)

class Director(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)