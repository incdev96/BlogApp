from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post

def post_list(request: HttpRequest) -> HttpResponse:
    posts: Post = Post.published.all()

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request: HttpRequest, year: int, month: int, day: int, post: Post) -> HttpResponse:
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )