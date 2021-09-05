from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ArticleForm, RunParseSiteForm
from .models import Article, Tag, Site
from django.urls import reverse
from django.core.paginator import Paginator
from .tasks import hello_world
from .services import run_parse_site


def article_list(request):
    queryset = Article.objects.all().prefetch_related('tags').prefetch_related('authors')
    paginator = Paginator(queryset, 15)
    page_numb = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_numb)
    context = {'page_obj': page_obj}
    return render(request, "article/article_list.html", context)

def article_detail(request, id):
    try:
        art = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {"art": art}
    return render(request, "article/article_detail.html", context)

def article_create(request):
    # for test Celery
    # hello_world.delay()

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

def article_parse(request):
    ''' запуск парсинга статей с определенного ресурса '''
    site = Site.objects.all()
    if request.method == "POST":
        site_name = request.POST.get("site_name")
        status = run_parse_site(site_name)
        return redirect('/article/')
    else:
        form = RunParseSiteForm()
    context = {'form': form}
    return render(request, "article/article_parse.html", context)
