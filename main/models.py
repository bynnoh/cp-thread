from django.db import models
from django.urls import reverse

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)

    likes = models.IntegerField(default=0, editable=False)
    down = models.IntegerField(default=0, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("thread_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    content = models.TextField(max_length=1000)

    likes = models.IntegerField(default=0, editable=False)
    down = models.IntegerField(default=0, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTImeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.thread.get_absolute_url()}#{self.pk}'
    