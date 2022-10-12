from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('share', views.share_movie, name='share_movie'),
]