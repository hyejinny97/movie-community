from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# 게시글 목록 조회
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

# 게시글 작성 페이지 및 게시글 데이터 생성
@login_required
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
    comment = CommentForm()

    context = {
        'article': article,
        'comment': comment,
    }

    return render(request, 'articles/detail.html', context)

# 게시글 수정
@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if article.writer == request.user:
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
    else:
        messages.warning(request, '게시글 수정 권한이 없습니다.')
        return redirect('articles:detail', article.pk)

# 게시글 삭제
@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.writer == request.user:
        article.delete()
        return redirect('articles:index')
    else:
        messages.warning(request, '게시글 삭제 권한이 없습니다.')
        return redirect('articles:detail', article.pk)

# comments 데이터 생성
@login_required
def comments(request, article_pk):
    form = CommentForm(request.POST)

    if form.is_valid():
        temp = form.save(commit=False)
        temp.writer = request.user
        temp.review_id = article_pk
        temp.save()

        return redirect('articles:detail', article_pk)

# comments 데이터 삭제
@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.writer == request.user:
        comment.delete()
        return redirect('articles:detail', article_pk)
    else:
        messages.warning(request, '댓글 삭제 권한이 없습니다.')
        return redirect('articles:detail', article_pk)