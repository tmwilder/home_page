#Django
from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def contact(request):
    #Add call to email func
    return render(request, 'main.html')
