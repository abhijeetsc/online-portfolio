from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    print(detailblog)
    return render(request, 'blog/detail.html', {'detailblog': detailblog})
