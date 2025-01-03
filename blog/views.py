from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post

def post_list(request: HttpRequest) -> HttpResponse:
    post_list: Post = Post.published.all()

    paginator = Paginator(post_list, 2)
    page_number: int = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request: HttpRequest, year: int, month: int, day: int, post: Post) -> HttpResponse:
    post = get_object_or_404(
        Post,
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