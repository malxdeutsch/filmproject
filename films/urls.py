from django.urls import path
from .views import AddFilmCreateView, AddDirectorCreateView, HomepageDetailView

urlpatterns = [
    path('homepage/', HomepageDetailView.as_view(), name = 'homepage'),
    path('addfilm/', AddFilmCreateView.as_view(), name = 'addfilm'),
    path('adddirector/', AddDirectorCreateView.as_view(), name = 'adddirector'),
]
