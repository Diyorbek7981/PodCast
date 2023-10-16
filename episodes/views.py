from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class EpisodesView(TemplateView):
    template_name = 'episode.html'