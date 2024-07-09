# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for listing posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL for post details
     path('post/new/', views.post_new, name='post_new'),
]
