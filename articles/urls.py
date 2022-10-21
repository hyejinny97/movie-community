from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # path('', views.index, name='index'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.detail, name='detail'),
]