from django.urls import path
from django.contrib import admin

from . import views

app_name='blog'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('<int:post_id>', views.detail, name='detail'),
    path('about', views.about , name='about'),
]