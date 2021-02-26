from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .infoUpdater import updater

updater.start()

def home_page(request):
    return render(request, 'esports/home.html')

