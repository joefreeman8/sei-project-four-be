from django.urls import path 
from .views import DogDetailView, DogListView, FavoriteListView, FavoriteDetailView

urlpatterns = [
    path('', DogListView.as_view()),
    path('<int:pk>/', DogDetailView.as_view()),
    path('<int:dog_pk>/favorites/', FavoriteListView.as_view()),
    path('<int:dog_pk>/favorites/<int:pk>/', FavoriteDetailView.as_view())
]
