from django.db import models

# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    likes = models.IntegerField(default=0, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)