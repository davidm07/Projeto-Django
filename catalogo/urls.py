from . import views
from django.urls import path

urlpatterns = [
    path('', views.getFilmes),
    path('<int:pk>/', views.FilmeById),
    path('genero/<str:genero>/', views.getFilmeByGenero),
]