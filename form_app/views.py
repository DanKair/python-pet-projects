from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .form import ContactForm
# Created 3 web-pages (templates) for the app

def home_page(request):
    return render(request, 'form_app/home.html')


def contact_page(request):
    # Check whether request method is POST request
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'form_app/contact.html', context)


def contact_success_page(request):
    return render(request, 'form_app/contact-success.html')