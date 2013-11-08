#Django
from django.shortcuts import render

def serve_main(request):
    return render('main.html')


def send_email(request):
    #Add call to email func
    return render('main.html')
