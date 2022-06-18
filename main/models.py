from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse

class Topic(models.Model):
    topic = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=10, unique=True, allow_unicode=True)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return f'/{self.slug}'

class Thread(models.Model):
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    upvotes = models.IntegerField(default=0, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/{self.pk}'

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    upvotes = models.IntegerField(default=0, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} | {self.content}'

    def get_absolute_url(self):
        return f'{self.thread.get_absolute_url()}#{self.pk}'

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint('user', 'thread', 'comment', name='user_and_tc')
        ]