from django.views.generic import ListView, CreateView, UpdateView
from .models import Movie
from .forms import MovieForm


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"


class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/movie_form.html"


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/movie_form.html"
