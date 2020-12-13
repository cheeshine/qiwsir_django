from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})


def blog_article(request, article_id):
    article = get_object_or_404(BlogArticles, id=article_id)  # get_object_or_404：没有object时，不执行下面内容，并返回404页面
    pub = article.publish
    return render(request, 'blog/content.html', {'article': article, 'publish': pub})
