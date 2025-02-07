from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, redirect
from django.utils import timezone

from mysite.forms import ContactForm
from mysite.models import Post, Works

def paginate(request, obj):
    paginator = Paginator(obj, 2)
    page = request.GET.get('page')
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
# Create your views here.
def main(request):
    posts = Post.objects.order_by('-date_posted')[:2]
    works = Works.objects.order_by('-date_posted')[:3]
    return render(request, 'main.html', {'posts': posts, 'works': works})

def works(request):
    works = Works.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    works = paginate(request, works)
    return render(request, 'works.html', {'works': works})

def post_list(request):
    posts = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
    posts = paginate(request, posts)
    return render(request, 'post_list.html', {'posts': posts})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            file = form.cleaned_data.get('file', None)

            email_message = EmailMessage(
                subject=f'Messege from {name} with email: {email}',
                body=message,
                from_email=email,
                to=[settings.CONTACT_EMAIL]
            )
            if file:
                email_message.attach(file.name, file.read(), file.content_type)
            email_message.send()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})