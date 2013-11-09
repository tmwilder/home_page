#Django
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
#home_page
from home_page_app.forms import ContactForm


def main(request):
    return render(request, 'main.html')


def contact(request):
    # raise(Exception(repr(request)))
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail('home_page user correspondence from {0}.'.format(name),
                      message,
                      sender_email,
                      [admin_email for _, admin_email in settings.ADMINS],
                      fail_silently=False)
        else:
            # raise Exception(repr(form))
            pass
    else:
        form = ContactForm()
    return render(request, 'main.html', {
        'form': form,
    })
