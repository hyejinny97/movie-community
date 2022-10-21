from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 게시글 목록 조회
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

# 게시글 작성 페이지 및 게시글 데이터 생성


def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.writer = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm()
    
    context = {
        'article_form': article_form,
    }

    return render(request, 'articles/article_create.html', context)

# 게시글 상세 페이지
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    print(article.title)
    if request.method =='POST':
        form = ArticleForm(request.POST, request.FILES ,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form
    }
    return render(request, 'articles/update.html',context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

