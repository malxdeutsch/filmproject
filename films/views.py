from django.shortcuts import render
from .models import Country, Category, Film, Director
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.

class FilmCreateView(CreateView):
    model = Film
    fields = '__all__'
    template_name = 'film/addfilm.html'
    success_url = reverse_lazy('homepage')


class DirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    template_name = 'director/adddirector.html'
    success_url = reverse_lazy('homepage')

class HomepageListView(ListView):
    queryset = Film.objects.all().order_by('-added_date')
    context_object_name = 'films'
    template_name = 'homepage.html'
