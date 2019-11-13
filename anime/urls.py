from django.urls import path, include
from .views import AnimeView, SearchResultsView, animeTest

app_name = 'anime'

urlpatterns = [
    #path('search/', SearchResultsView.as_view(), name='search_results'),
    #path('anime/', AnimeView.as_view(), name='home'),
    #path('', SearchResultsView.as_view(), name='search_reuslts')
    path('anime/', animeTest)
]
