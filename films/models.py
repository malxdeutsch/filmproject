from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length = 200)

class Category(models.Model):
    name = models.CharField(max_length = 200)

class Film(models.Model):
    title = models.CharField(max_length = 200)
    release_date = models.DateField ()
    created_in_country = models.ForeignKey(Country, on_delete = models.CASCADE)
    available_in_countries = models.ManyToManyField(Country)
    category = models.ManyToManyField(Category)
    director : models.ManyToManyField('Director')

class Director(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)