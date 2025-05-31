from django.urls import path
from .views import MovieListView, MovieCreateView, MovieUpdateView

app_name = "movies"

urlpatterns = [
    path("", MovieListView.as_view(), name="list"),
    path("add/", MovieCreateView.as_view(), name="add"),
    path("<int:pk>/edit/", MovieUpdateView.as_view(), name="edit"),
]
