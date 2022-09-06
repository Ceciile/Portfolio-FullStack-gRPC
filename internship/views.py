from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import Intern
from .forms import InternForm

def newinput(request):
    jobs = Intern.objects.all()
    
    if request.method == 'POST':
        form = InternForm(request.POST)
        if form.is_valid():
            # get Form Data
            cleaned_data = form.cleaned_data
            intern = Intern()
            intern.job_title = cleaned_data['job_title']
            intern.company_name = cleaned_data['company_name']
            intern.postal = cleaned_data['postal']
            intern.started_time=cleaned_data['started_time']
            intern.save()
            context = {
                'jobs': jobs,
                'form': form,
            }
            return HttpResponseRedirect(reverse('newIntern'))
    else:
        form = InternForm()
        print('GET method.')

    # avoid redirect
    return render(request, 'index.html', context=context)