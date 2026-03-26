from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.create_movie),
    path('movies/bulk', views.bulk_create_movies),
    path('movies/<int:pk>', views.update_movie),
    path('movies/list', views.get_movies),
    path('movies/<int:pk>/detail', views.get_movie),
]