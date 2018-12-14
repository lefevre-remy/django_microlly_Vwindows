from django.urls import path

from microblog import views

app_name = 'microblog'
urlpatterns = [
    path('', views.index, name='index'),
    #path('create/', views.post_create, name='create'),
]
