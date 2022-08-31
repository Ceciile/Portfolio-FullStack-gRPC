from django.shortcuts import render

# Create your views here.
from .models import Intern

def index(request):
    #words = 'FullStack!'
    jobs = Intern.objects.all()
    return render(request, 'index.html', context={'jobs': jobs})