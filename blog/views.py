from django.shortcuts import render
# from django.views import View
from django.views.generic import ListView, DetailView
from .models import Article

class Index(ListView):
    print("hi")
    model=Article
    queryset = Article.objects.all().order_by('-date')
    template_name='blog/index.html'
    print(queryset)

class DetailPage(DetailView):
    model=Article
    template_name='blog/blog_post.html'