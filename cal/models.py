from django.db import models
from markdownx.models import MarkdownxField

class Platform(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class Event(models.Model):
    event = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL)
    desc = MarkdownxField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.event} | {self.start}-{self.end}'
