from datetime import timedelta, date
from django.shortcuts import render

from blog.models import Post


def home_view(request):
    editors_pick = Post.objects.filter(editors_pick=True).last()
    trending_posts = Post.objects.filter(trending=True)[:3]
    week_ago = date.today() - timedelta(days=7)
    popular_post = Post.objects.filter(
        created_at__gte=week_ago).order_by('-hit_count').last()
    recent_posts = Post.objects.all()[:5]
    return render(request, 'index.html', {'editors_pick': editors_pick,
                                          'trending_posts': trending_posts,
                                          'popular_post': popular_post,
                                          'recent_posts': recent_posts})


def posts_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})
