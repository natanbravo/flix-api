from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(),
         name='review-create-list-view'),

    path('review/<int:pk>/', views.ReviewRetrieveUpdateDestroy.as_view(),
         name='review-detail-view'),
]
