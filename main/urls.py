from django.urls import path

from . import views

urlpatterns = [
    path('', views.ThreadList.as_view()),
    path('<str:slug>', views.topic_page),
    path('<int:pk>', views.ThreadDetail.as_view(), name='thread-detail'),
]