from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Topic, Thread, Comment, Vote
from .forms import ThreadForm, CommentForm

class ThreadList(ListView):
    model = Thread
    paginate_by = 10

    ordering = ['-upvotes']

# class ThreadDetail(DetailView):
#     model = Thread

class ThreadCreate(CreateView):
    model = Thread
    form_class = ThreadForm

    # def get_context_data(self, **kwargs):
    #     context = super(ThreadCreate, self).get_context_data(**kwargs)
    #     context['image'] = self.request.FILES
    #     return context

# def submit_thread(request):
#     if request.method == 'POST':
#         form = ThreadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ThreadForm()

#     thread = get_object_or_404(Thread, pk=request.pk)

#     return render(
#         request,
#         'main/thread_detail.html',
#         thread
#     )

class CommentList(ListView):
    model = Comment

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment
    fields = ['content', 'image']
    # http_method_names = ['POST']
    # template_name = 'thread_detail.html'
    # model = Comment
    # form_class = CommentForm

    # def form_valid(self, form):
    #     form.instance.thread = Thread.objects.get(pk=self.kwargs.get("pk"))
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('thread-detail', kwargs={'pk': self.kwargs.get("pk")})

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    form = CommentForm()

    return render(
        request,
        'main/thread_detail.html',
        {
            'thread': thread, 
            'form': form
        }
    )

def submit_comment(request, pk):
    thread = Thread.objects.get(pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        form.save(commit=False)
        form.instance.thread = thread
        form.save()
        return redirect(thread.get_absolute_url())

    else:
        return redirect(thread.get_absolute_url())

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
    vote = Vote.objects.filter(thread=target)

    if vote.filter(user=request.user):
        return redirect(target.get_absolute_url())
    else:
        Vote.objects.create(user = request.user, thread = target)
        target.upvotes += 1
        target.save()
        return redirect(target.get_absolute_url())


def downvote_thread(request, pk):
    target = get_object_or_404(Thread, id=pk)
    vote = Vote.objects.filter(thread=target)

    if vote.filter(user=request.user):
        return redirect(target.get_absolute_url())
    else:
        Vote.objects.create(user = request.user, thread = target)
        target.upvotes -= 1
        target.save()
        return redirect(target.get_absolute_url())