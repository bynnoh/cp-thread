from django.urls import path

from . import views

urlpatterns = [
    path('', views.ThreadList.as_view()),
    path('<int:pk>', views.thread_detail, name='thread-detail'),
    path('<int:pk>/submit-comment', views.submit_comment, name='submit-comment'),
    path('upvote/<int:pk>', views.upvote_thread, name='upvote'),
    path('topic/<str:slug>', views.topic_page),
    path('submit', views.ThreadCreate.as_view()),
]