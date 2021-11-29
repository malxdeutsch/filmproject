from django.shortcuts import render
from .models import Country, Category, Film, Director
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.

class AddFilmCreateView(CreateView):
    model = Film
    fields = '__all__'
    template_name = 'addfilm.html'
    success_url = reverse_lazy('homepage')


class AddDirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    template_name = 'addtemplate.html'
    success_url = reverse_lazy('homepage')

class HomepageDetailView(ListView):
    model = Film
   
