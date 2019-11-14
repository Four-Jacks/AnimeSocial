from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Anime
from anime.forms import AnimeForm


# Create your views here.
class AnimeView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Anime
    template_name = 'search_results.html'

    def get_queryset(self, request):
        form = AnimeForm
        query = self.request.GET.get('q')
        object_list = Anime.objects.filter(
            Q(title__icontains=query)
        )
        return render(request, self.template_name, object_list, {'form': form})
