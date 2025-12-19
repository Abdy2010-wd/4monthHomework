from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, MovieListView, MovieDetailView  # и другие CBV

urlpatterns = [
    path('login/', LoginView.as_view(template_name='cineboard/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='movie_list'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),

]

