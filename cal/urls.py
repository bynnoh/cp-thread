from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.EventList.as_view()),
]
