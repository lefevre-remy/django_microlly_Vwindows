from django.urls import path

from microblog import views

app_name = 'microblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.article_create, name='article_create'),
    path('detail/', views.article_detail, name='article_detail'),
    path('list/', views.article_list, name='article_list'),
]
