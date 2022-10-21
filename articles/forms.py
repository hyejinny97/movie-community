from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('movie_name', 'title', 'content', 'grade', 'image', 'thumbnail',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)