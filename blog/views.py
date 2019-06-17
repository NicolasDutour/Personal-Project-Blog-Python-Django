from django.shortcuts import render
from .models import Post


def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_index.html', context)
