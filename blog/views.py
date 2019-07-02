from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_index.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return redirect('blog_index')

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/post_detail.html", context)
