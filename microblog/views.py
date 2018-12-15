from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from microblog.models import Post

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts':post})

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'microblog/article_list.html', { 'articles': articles })

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'article_detail.html', { 'article': article })

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('microblog:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'microblog/article_create.html', { 'form': form })
