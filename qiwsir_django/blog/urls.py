from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_title),
    path('<int:article_id>/', views.blog_article),
]
