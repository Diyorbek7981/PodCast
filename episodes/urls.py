from django.urls import path
from .views import *


urlpatterns = [
    path('',EpisodesView.as_view(),name='episodes'),
]