from django.urls import path
from .views import FilmCreateView, DirectorCreateView, HomepageListView

urlpatterns = [
    path('homepage/', HomepageListView.as_view(), name = 'homepage'),
    path('addfilm/', FilmCreateView.as_view(), name = 'addfilm'),
    path('adddirector/', DirectorCreateView.as_view(), name = 'adddirector'),
]
