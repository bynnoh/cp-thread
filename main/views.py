from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render

from .models import Topic, Thread, Comment

class ThreadList(ListView):
    model = Thread

class ThreadDetail(DetailView):
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

def topic_page(request, slug):
    topic = Topic.objects.get(slug=slug)
    thread_list = Thread.objects.filter(topic=topic)

    context = {
        'topic': topic,
        'thread_list': thread_list
    }

    return render(
        request,
        'main/thread_list.html',
        context
    )