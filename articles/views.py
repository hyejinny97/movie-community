from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
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