from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Game, Review


class GameListView(ListView):
    model = Game
    template_name = "gamereview/gamelist.html"
    context_object_name = "games"


class ReviewView(DetailView):
    model = Game
    template_name = "gamereview/review.html"
    context_object_name = "game"
