from django.views.generic import ListView
from django.shortcuts import render

from .models import Thread

# Create your views here.

class ThreadList(ListView):
    model = Thread
