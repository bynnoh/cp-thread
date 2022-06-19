from django.contrib import admin
from .models import Topic, Thread, Comment, Vote
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Thread, MarkdownxModelAdmin)
admin.site.register(Comment)

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('topic', )}

admin.site.register(Topic, TopicAdmin)

admin.site.register(Vote)
