from typing import List
from xml.etree.ElementTree import Comment
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render

from .models import Thread, Comment

# Create your views here.

class ThreadList(ListView):
    model = Thread

class ThreadDetai(DetailView):
    model = Thread

class ThreadCreate(CreateView):
    model = Thread
    fields = ['title', 'content']

class CommentList(ListView):
    model = Comment

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment