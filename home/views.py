from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """ View to return index page """

    return render(request, 'home/index.html')