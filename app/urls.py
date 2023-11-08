from django.contrib import admin
from django.urls import path

from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroy
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroy


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-list'),
    path('genre/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),

    path('actors/', ActorCreateListView.as_view(), name='actor-create-list-view'),
    path('actor/<int:pk>/', ActorRetrieveUpdateDestroy.as_view(), name='actor-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movie-create-list-view'),
    path('movie/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list-view'),
    path('review/<int:pk>/', ReviewRetrieveUpdateDestroy.as_view(), name='review-detail-view')
]
