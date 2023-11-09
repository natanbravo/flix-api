from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(),
         name='actor-create-list-view'),
         
    path('actor/<int:pk>/', views.ActorRetrieveUpdateDestroy.as_view(),
         name='actor-detail-view'),
]
