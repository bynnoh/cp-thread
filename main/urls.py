from django.urls import path

from . import views

urlpatterns = [
    path('', views.ThreadList.as_view()),
]