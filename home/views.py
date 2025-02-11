from django.shortcuts import render
from blog.models import Post
from works.models import Work

# Create your views here.
def main(request):
    posts = Post.objects.order_by('-publish')[:2]
    works = Work.objects.order_by('-publish')[:3]
    return render(request, 'home/main.html', {'posts': posts, 'works': works})