from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q, Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Movie

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'CineBoard/signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'CineBoard/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class MovieListView(ListView):
    model = Movie
    template_name = 'CineBoard/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_queryset(self):
        queryset = Movie.objects.all()

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)

        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(tags__name__icontains=genre)

        queryset = queryset.annotate(avg_rating=Avg('rating')).order_by('-avg_rating')

        return queryset

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'CineBoard/movie_detail.html'
    context_object_name = 'movie'

class MovieCreateView(CreateView):
    model = Movie
    template_name = 'CineBoard/movie_form.html'
    fields = ['title', 'description', 'genre', 'release_date']  
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'CineBoard/movie_form.html'
    fields = ['title', 'description', 'genre', 'release_date']
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'CineBoard/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')
