from django.urls import path
from movie import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'movie'
urlpatterns = [
    path('allmovies', views.movielist, name='allmovies'),
    path('addmovie', views.add_movie, name='addmovie'),
    path('singlemovie/<slug:singlemovie_name_slug>/', views.singlemovie, name='singlemovie'),
    path('addreview', views.add_review, name='addreview'),
    path('<int:movie_id>/', views.ReviewView.as_view(), name='review'),
] 