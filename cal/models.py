from django.db import models
from markdownx.models import MarkdownxField

class Event(models.Model):
    event = MarkdownxField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.event} | {self.start}-{self.end}'