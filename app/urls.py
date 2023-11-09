from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('genres.urls')),

    path('api/v1/', include('actors.urls')),

    path('api/v1/', include('movies.urls')),

    path('api/v1/', include('reviews.urls')),
]
