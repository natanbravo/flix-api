from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(),
         name='movie-create-list-view'),

    path('movie/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(),
         name='movie-detail-view'),
]
