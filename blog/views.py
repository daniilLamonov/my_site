from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post_detail.html', {'post': post})