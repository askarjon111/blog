from django.urls import path
from blog.views import home_view, posts_view


urlpatterns = [
    path('', home_view, name='home'),
    path('posts/', posts_view, name='posts'),
]

