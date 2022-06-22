from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ThreadList.as_view()),
    path('<int:pk>', views.thread_detail, name='thread-detail'),
    path('<int:pk>/update', views.ThreadUpdate.as_view(), name='thread-update'),
    path('<int:pk>/submit-comment', views.submit_comment, name='submit-comment'),
    path('<int:pk>/submit-reply', views.submit_reply, name="submit-reply"),
    path('markdownx/', include('markdownx.urls')),
    path('upvote/<int:pk>', views.upvote_thread, name='upvote'),
    path('downvote/<int:pk>', views.downvote_thread, name='downvote'),
    path('upvote-comment/<int:pk>', views.upvote_comment, name='upvote-comment'),
    path('downvote-comment/<int:pk>', views.downvote_comment, name='downvote-comment'),
    path('topic/<str:slug>', views.topic_page),
    path('submit', views.ThreadCreate.as_view()),
]