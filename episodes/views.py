from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from episodes.models import Podcast, Category, Tags


# Create your views here.

class EpisodesView(ListView):
    template_name = 'episodes.html'
    model = Podcast
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tags.objects.all()
        return context


class EpisodeView(DetailView):
    template_name = 'episode.html'
    model = Podcast
    context_object_name = 'podcast'
