from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import TextInputForm

def index(request):
    context ={}
    context['form']= TextInputForm()
    return render(request, "index.html", context)