from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('test',views.home, name='home')
]
