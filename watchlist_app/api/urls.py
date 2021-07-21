from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path('list/', views.MovieListAV.as_view()),
    path('<int:pk>', views.MovieDetailsAV.as_view()),
]





# from watchlist_app.api import views
# urlpatterns = [
#     # path('', views.home, name='home'),
#     path('list/', views.movie_list, name='movie-list'),
#     path('<int:pk>', views.movie_details, name='movie-details'),
# ]