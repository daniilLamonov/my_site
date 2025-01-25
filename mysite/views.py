from django.shortcuts import render
from django.utils import timezone
from mysite.models import Post, Works


# Create your views here.
def main(request):
    posts = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request, 'main.html', {'posts': posts})

def works(request):
    works = Works.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request, 'works.html', {'works': works})

def post_list(request):
    posts = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    return render(request, 'post_list.html', {'posts': posts})

def contacts(request):
    return render(request, 'contacts.html')