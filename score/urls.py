from django.urls import path
from . import views

urlpatterns = [
  path("hello/", views.hello, name='hello'),
  path("get_score/", views.get_score, name='get_score'),
  
]