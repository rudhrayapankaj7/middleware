# file: middleware_demo/urls.py

from django.urls import path
from .views import index

urlpatterns = [
    path("demo/", index),
]