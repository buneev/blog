from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ArticleForm
from .models import Article, Tag
from django.urls import reverse
from django.core.paginator import Paginator


def article_list(request):
    queryset = Article.objects.all()
    paginator = Paginator(queryset, 5)
    page_numb = request.GET.get('page', 1)
    page = paginator.get_page(page_numb)
    context = {"article_list": page}
    return render(request, "article/article_list.html", context)

def article_detail(request, id):
    try:
        art = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {"art": art}
    return render(request, "article/article_detail.html", context)

def article_create(request):
    init_data = {'title': ''}
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect()
    else:
        form = ArticleForm(initial=init_data)
    context = {'form': form}
    return render(request, "article/article_create.html", context)

def article_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'article': article}
    return render(request, "article/article_update.html", context)

def article_delete(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        article.delete()
        url = reverse('article:article_list_url')
        return redirect(url)
    context = {'article': article}
    return render(request, "article/article_delete.html", context)

def tag_detail(request, name):
    tag = Tag.objects.get(title=name)
    context = {"tag": tag}
    return render(request, "article/tag_detail.html", context)
