'''
from django.urls import path
from . import views
urlpatterns = [
    #path('', views.home, name='home'),
    path('list/', views.movie_list, name='movie-list'),
    path('<int:pk>', views.movie_details, name='movie-details')
]
'''