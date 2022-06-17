from django.urls import path

from . import views

urlpatterns = [
    path('', views.ThreadList.as_view()),
    path('submit', views.ThreadCreate.as_view()),
    path('<int:pk>', views.ThreadDetail.as_view(), name='thread-detail'),
    path('upvote/<int:pk>', views.upvote_thread, name='upvote'),
    path('topic/<str:slug>', views.topic_page),
]