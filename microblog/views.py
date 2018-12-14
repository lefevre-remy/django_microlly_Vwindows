from django.shortcuts import render
from microblog.models import Post

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts':post})