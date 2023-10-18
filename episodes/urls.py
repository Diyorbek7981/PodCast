from django.urls import path
from .views import *

urlpatterns = [
    path('', EpisodesView.as_view(), name='episodes'),
    path('<int:pk>', EpisodeView.as_view(), name='episode'),
]
