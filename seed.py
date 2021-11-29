from faker import Faker
import os
import django
import random

fake = Faker()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FilmProject.settings')
django.setup()

from films.models import Country, Category, Film, Director

def create_country():
    for _ in range(10):
        Country.objects.create(name = fake.country())

# create_country()

def create_category():
    categories = ['Comedy', 'Action', 'Rom-Com', 'Mystery']
    for category in categories:
        Category.objects.create (name = category)
        
# create_category()

def create_film():
    for _ in range (5):
        Vehicle.objects.create(title = fake.movie.title(),
        release_date = fake.date(),
        created_in_country = models.random.choice(Country.objects.all()),
        available_in_countries = models.random.choice(Country.objects.all()),
        category = models.random.choice(Category.objects.all()),
        director = models.random.choice(Director.objects.all()))

# create_film()
