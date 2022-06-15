from django.contrib import admin
from .models import Topic, Thread, Comment

admin.site.register(Thread)
admin.site.register(Comment)

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('topic', )}

admin.site.register(Topic, TopicAdmin)
