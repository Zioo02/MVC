from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField("Tytuł", max_length=120)
    director = models.CharField("Reżyser", max_length=120)
    rating = models.DecimalField("Ocena", max_digits=3, decimal_places=1)

    class Meta:
        ordering = ["-rating", "title"]

    def __str__(self):
        return f"{self.title} ({self.director})"

    def get_absolute_url(self):
        return reverse("movies:list")
