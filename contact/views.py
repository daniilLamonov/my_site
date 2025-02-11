from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from contact.forms import ContactForm
from my_site import settings


# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            file = form.cleaned_data.get('file', None)
            email_message = EmailMessage(
                subject=f'Message from {name} with {email}',
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
            messages.error(request, form.errors)
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})
