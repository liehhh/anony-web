from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='confess-home'),
    path('story/<int:pk>/', views.story, name='confess-story'),
    path('search_results', views.search_results, name='confess-search_results'),
    path('create', views.create, name='confess-create'),
]
