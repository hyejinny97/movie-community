from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('movie_name', 'title', 'content', 'grade', 'image', 'thumbnail',)