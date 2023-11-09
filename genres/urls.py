from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-list'),

    path('genre/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(),
         name='genre-detail-view'),
]
