from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect, render

from .models import Topic, Thread, Comment, Vote

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

def upvote_thread(request, pk):
    target = get_object_or_404(Thread, id=pk)
    Vote.objects.create(user = request.user, thread = target)
    target.upvotes += 1
    target.save()
    
    return redirect(target.get_absolute_url())