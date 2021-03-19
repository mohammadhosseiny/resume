from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from portfolio_contact.forms import ContactForm, ContactForm_Fa
from portfolio_contact.models import Contact


def contact_me(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        message = contact_form.cleaned_data.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        send_mail(subject, f'You have an email from : {email}\n\nName : {name}\n\n{message}',
                  'Your Site Resume', ['dev.mohammadhosseiny@gmail.com'], fail_silently=False)
        messages.success(request, 'Your Message Successfully Sent')
        contact_form = ContactForm()
        return redirect('/')

    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact_form.html', context)


def contact_me_fa(request):
    contact_form = ContactForm_Fa(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        message = contact_form.cleaned_data.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        send_mail(subject, f'You have an email from : {email}\n\nName : {name}\n\n{message}',
                  'Your Site Resume', ['dev.mohammadhosseiny@gmail.com'], fail_silently=False)
        messages.success(request, 'پیام شما با موفقیت ارسال شد')
        contact_form = ContactForm()
        return redirect('/fa')

    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact-form-fa.html', context)
